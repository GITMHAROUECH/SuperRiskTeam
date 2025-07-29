from app.tool.base import BaseTool, ToolResult, ToolFailure

class FileWriter(BaseTool):
    name: str = "file_writer"
    description: str = "Écrit du contenu dans un fichier local."

    async def execute(self, path: str, content: str) -> ToolResult:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return ToolResult(result=f"Écrit dans {path}")
        except Exception as e:
            return ToolFailure(error=str(e))
