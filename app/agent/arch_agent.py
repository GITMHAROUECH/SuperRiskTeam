from app.agent.base import BaseAgent
from app.llm import LLM
from app.tool import Tool

class ArchAgent(BaseAgent):
    """
    Agent Architecte :
    - Conçoit l’architecture technique (modules Python, services, schéma de base de données)
    - Définit les dépendances, l’organisation du code et les bonnes pratiques CI/CD
    """

    def __init__(self):
        super().__init__(
            name="ArchAgent",
            description=(
                "Définit l’architecture technique, la structure des modules, "
                "le schéma de données et les pipelines CI/CD."
            ),
            llm=LLM(),
            tools=[
                Tool.CreateChatCompletion,
                Tool.PlanningTool,
            ],
        )

    async def run(self, input_data: str) -> str:
        """
        input_data : spécifications fonctionnelles produites par SpecAgent
        """
        return await super().run(input_data)

    async def step(self):
        """
        Délègue l’exécution d’une étape au BaseAgent
        """
        return await super().step()
