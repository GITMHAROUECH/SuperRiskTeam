# app/agent/dev_agent.py

from app.agent.base import BaseAgent
from app.llm import LLM
from app.tool import Tool

class DevAgent(BaseAgent):
    """
    Agent Développeur :
    prend en entrée une architecture technique ou des spécifications détaillées
    et génère le code source correspondant, prêt à être exécuté ou testé.

    Livrables typiques :
      - Fichiers Python organisés (modules, classes, fonctions)
      - Commentaires et docstrings
      - Scripts de mise en place (requirements.txt, Dockerfile…)
      - Instructions d’exécution
    """

    def __init__(self):
        super().__init__(
            name="DevAgent",
            description=(
                "Agent Développeur Python : génère du code opérationnel "
                "selon l’architecture définie, avec bonnes pratiques et documentation."
            ),
            llm=LLM(),
            tools=[
                Tool.PythonExecute,   # Exécute et valide le code généré
                Tool.WebSearch        # Optionnel, pour rechercher des exemples ou bibliothèques
            ]
        )

    async def run(self, input_doc: str) -> str:
        """
        Exécuté avec :
            await DevAgent().run(architecture_technique)

        Retourne :
        Le code source complet (en un ou plusieurs fichiers) sous forme textuelle,
        prêt à être enregistré et exécuté.
        """
        return await super().run(input_doc)

    # **Ajoutez cette méthode pour lever l’abstraction**
    async def step(self):
        """
        Délègue l’exécution d’une étape à la classe de base.
        """
        return await super().step()
