# app/agent/test_agent.py

from app.agent.base import BaseAgent
from app.llm import LLM
from app.tool import Tool

class TestAgent(BaseAgent):
    """
    Agent QA / Testeur :
    prend en entrée le code source ou le projet généré et produit :
      1. Un plan de tests unitaires et d’intégration
      2. Les scripts de tests (pytest, unittest…)
      3. Un rapport de couverture et de résultats
      4. Les recommandations de corrections en cas d’échec
    """

    def __init__(self):
        super().__init__(
            name="TestAgent",
            description=(
                "Agent QA/Testeur : génère et exécute des tests pour valider "
                "le code selon les spécifications, et produit un rapport clair."
            ),
            llm=LLM(),
            tools=[
                Tool.PythonExecute,    # Pour lancer pytest ou scripts de tests
                Tool.FileReader,       # Pour lire le code source
                Tool.FileWriter        # Pour écrire les fichiers de test
            ]
        )

    async def run(self, code_text: str) -> str:
        """
        Exécuté avec :
            await TestAgent().run(code_text)

        Retourne :
        1. Les fichiers de tests générés (ex. test_*.py)
        2. Le log d'exécution des tests (succès / échecs)
        3. Un mini‐rapport de couverture et recommandations
        """
        return await super().run(code_text)

    # **Ajoutez cette méthode pour lever l’abstraction**
    async def step(self):
        """
        Délègue l’exécution d’une étape à la classe de base.
        """
        return await super().step()
