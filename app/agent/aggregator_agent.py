from app.agent.base import BaseAgent
from app.llm import LLM
from app.tool import Tool

class AggregatorAgent(BaseAgent):
    """
    Agent Agrégateur :
    - Assemble tous les artefacts générés (spécifications, architecture, code, tests, validations réglementaires)
    - Produit la documentation finale et un package prêt à déployer (README, guide d’installation, structure de dossier)
    """

    def __init__(self):
        super().__init__(
            name="AggregatorAgent",
            description=(
                "Compile les livrables intermédiaires, génère la documentation finale, "
                "un guide d’installation et organise la structure de projet."
            ),
            llm=LLM(),
            tools=[
                Tool.FileReader,
                Tool.FileWriter,
                Tool.Calculator,
            ],
        )

    async def run(self, inputs: str) -> str:
        """
        inputs : concaténation de tous les artefacts générés par les autres agents
        """
        return await super().run(inputs)

    async def step(self):
        """
        Délègue l'exécution d'une étape à la classe de base
        """
        return await super().step()
