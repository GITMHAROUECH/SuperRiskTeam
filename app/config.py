import os
import tomllib
from pathlib import Path
from pydantic import BaseModel, Field

# Project root is two levels up (from app/config.py to project root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# Expect a config/config.toml at the project root, or config.toml
CONFIG_PATHS = [
    PROJECT_ROOT / "config" / "config.toml",
    PROJECT_ROOT / "config.toml",
]

class SandboxSettings(BaseModel):
    base_path: str = Field(..., description="Path to the sandbox directory")
    timeout: int = Field(60, description="Execution timeout in seconds")

class LLMSettings(BaseModel):
    """
    Generic LLM configuration.
    """
    provider: str = Field(..., description="LLM provider, e.g. 'openai'")
    model: str = Field(..., description="Model name, e.g. gpt-4-turbo")
    api_key: str = Field(..., description="API key")
    base_url: str = Field(..., description="Base URL, e.g. https://api.openai.com/v1")
    api_version: str = Field("", description="Optional API version (for Azure OpenAI)")

class AppConfig(BaseModel):
    llm: LLMSettings

class Config:
    _instance: "Config" = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load()
        return cls._instance

    def _load(self):
        config_path = next((p for p in CONFIG_PATHS if p.exists()), None)
        if config_path is None:
            raise FileNotFoundError(
                f"Configuration file not found. Checked: {[str(p) for p in CONFIG_PATHS]}"
            )

        with config_path.open("rb") as f:
            raw = tomllib.load(f)

        llm_root = raw.get("llm", {})
        if isinstance(llm_root, dict) and "default" in llm_root and isinstance(llm_root["default"], dict):
            section = llm_root["default"]
        else:
            section = llm_root

        provider = section.get("provider")
        model = section.get("model")
        api_key = section.get("api_key")
        base_url = section.get("base_url")
        api_version = section.get("api_version", "")

        if isinstance(api_key, str) and api_key.startswith("${") and api_key.endswith("}"):
            env_var = api_key[2:-1]
            api_key = os.getenv(env_var)
            if not api_key:
                raise RuntimeError(f"Environment variable '{env_var}' not set for api_key")

        if not api_key or not base_url or not model:
            raise RuntimeError(
                f"LLM configuration missing 'api_key', 'base_url', or 'model' in {config_path}"
            )

        self.app = AppConfig(
            llm=LLMSettings(
                provider=provider,
                model=model,
                api_key=api_key,
                base_url=base_url,
                api_version=api_version,
            )
        )

    @property
    def llm(self) -> LLMSettings:
        return self.app.llm

# Singleton instance
config = Config()
