# app/agent/regulatory_agent.py
from app.agent.base import BaseAgent
from app.llm import LLM
from app.tool import Tool

class RegulatoryExpertAgent(BaseAgent):
    """
    Expert réglementaire (CRR3, COREP/EBA) :
    - Connaît l’intégralité des normes EBA pour solvabilité et reporting
    - Valide architecture, code et tests selon ces règles
    """
    def __init__(self):
        super().__init__(
            name="RegulatoryExpert",
            description="Expert unifié CRR3/COREP/EBA pour valider specs, code et tests",
            llm=LLM(),
            tools=[
                Tool.FileReader,    # CRR3.pdf, XSD COREP
                Tool.WebSearch,
                Tool.Calculator
            ]
        )
    async def run(self, prompt: str) -> str:
        return await super().run(prompt)

    # **Ajoutez cette méthode pour lever l’abstraction**
    async def step(self):
        """
        Délègue l’exécution d’une étape à la classe de base.
        """
        return await super().step()
