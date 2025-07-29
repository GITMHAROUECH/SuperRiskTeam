from app.agent.base import BaseAgent
from app.llm import LLM
from app.tool import Tool

class SpecAgent(BaseAgent):
    """
    Agent Product Owner :
    - Rédige les spécifications fonctionnelles à partir du besoin métier.
    """

    def __init__(self):
        super().__init__(
            name="SpecAgent",
            description="Produit les spécifications fonctionnelles détaillées.",
            llm=LLM(),
            tools=[
                Tool.CreateChatCompletion,
                Tool.WebSearch,
            ],
        )

    async def run(self, input_data: str) -> str:
        """
        input_data : description du besoin métier
        """
        return await super().run(input_data)

    async def step(self):
        """
        Délègue l'exécution d'une étape à la classe de base
        """
        return await super().step()
