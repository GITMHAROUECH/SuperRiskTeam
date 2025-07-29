from app.tool.base import BaseTool, ToolResult, ToolFailure

class Calculator(BaseTool):
    name: str = "calculator"
    description: str = "Évalue une expression mathématique simple."

    async def execute(self, expression: str) -> ToolResult:
        try:
            result = eval(expression, {"__builtins__": {}})
            return ToolResult(result=str(result))
        except Exception as e:
            return ToolFailure(error=str(e))
