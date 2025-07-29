# app/tool/__init__.py

from types import SimpleNamespace

# --- Outils de base (modèles Pydantic) ---
from .base import BaseTool, ToolResult, ToolFailure

# --- Nouveaux outils personnalisés ---
from .file_reader import FileReader
from .file_writer import FileWriter
from .calculator import Calculator
from .python_execute import PythonExecute

# --- Outils existants dans ton projet ---
from .bash import Bash
from .browser_use_tool import BrowserUseTool
from .create_chat_completion import CreateChatCompletion
from .planning import PlanningTool
from .str_replace_editor import StrReplaceEditor
from .terminate import Terminate
from .web_search import WebSearch
from .crawl4ai import Crawl4aiTool

# (Optionnel) Enum ou collection initiale d’outils
from .tool_collection import ToolCollection

# --- Alias unique pour importer tous les outils via `Tool` ---
Tool = SimpleNamespace(
    # Outils de base
    FileReader=FileReader,
    FileWriter=FileWriter,
    Calculator=Calculator,
    PythonExecute=PythonExecute,
    # Outils internes
    Bash=Bash,
    BrowserUseTool=BrowserUseTool,
    CreateChatCompletion=CreateChatCompletion,
    PlanningTool=PlanningTool,
    StrReplaceEditor=StrReplaceEditor,
    Terminate=Terminate,
    WebSearch=WebSearch,
    Crawl4aiTool=Crawl4aiTool,
    # (éventuellement) collection enum
    ToolCollection=ToolCollection,
)

# Exports publics
__all__ = [
    "BaseTool", "ToolResult", "ToolFailure",
    "FileReader", "FileWriter", "Calculator",
    "Bash", "BrowserUseTool", "CreateChatCompletion",
    "PlanningTool", "StrReplaceEditor", "Terminate",
    "WebSearch", "Crawl4aiTool",
    "ToolCollection",
    "Tool",
]
