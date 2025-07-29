# app/agent/simulation_agent.py

from app.agent.base import BaseAgent
from app.llm import LLM
from app.tool import Tool

class SimulationAgent(BaseAgent):
    """
    Agent de Simulation :
    - Conçoit et exécute des scénarios de simulation financière (stress tests, hypothèses macroéconomiques)
    - Génère des jeux de données structurés (CSV/JSON) pour la phase de calcul
    """

    def __init__(self):
        super().__init__(
            name="SimulationAgent",
            description=(
                "Agent Simulation : crée et exécute des scénarios de simulation financière "
                "(stress tests, variations macro), et produit un jeu de données prêt pour le calcul."
            ),
            llm=LLM(model="gpt-4-turbo"),
            memory=True,
            tools=[
                Tool.WebSearch,     # Pour récupérer des indicateurs macro ou benchmarks
                Tool.PythonExecute, # Pour générer et valider les datasets via script
                Tool.FileWriter     # Pour enregistrer les jeux de données en sortie
            ]
        )

    async def run(self, prompt: str) -> str:
        """
        Exécuté avec :
            await SimulationAgent().run("Définir un scénario de stress 2025 : PIB -3%, taux +150bps…")

        Paramètre `prompt` :
        - Description du scénario de simulation (période, variables, amplitude, fréquences)
        
        Retourne :
        - Chemin vers le fichier de données généré (ex. 'output/sim_data_2025.csv')
        - Brève synthèse du contenu des données (nombre de lignes, colonnes, variables)
        """
        return await super().run(prompt)
