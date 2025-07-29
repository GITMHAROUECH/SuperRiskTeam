from app.tool.base import BaseTool, ToolResult, ToolFailure

class FileReader(BaseTool):
    name: str = "file_reader"
    description: str = "Lit un fichier local et renvoie son contenu."

    async def execute(self, path: str) -> ToolResult:
        try:
            with open(path, encoding="utf-8") as f:
                content = f.read()
            return ToolResult(result=content)
        except Exception as e:
            return ToolFailure(error=str(e))
