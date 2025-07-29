# app/agent/corep_agent.py

from app.agent.base import BaseAgent
from app.llm import LLM
from app.tool import Tool

class CorepAgent(BaseAgent):
    """
    Agent Expert COREP :
    connaît toutes les règles et spécifications EBA pour produire les rapports
    COREP (Common Reporting) conformes aux exigences réglementaires.

    Livrables typiques :
      - Fichiers XML/CSV COREP (template EBA)
      - Documentation des calculs (ratios, colonnes, niveaux)
      - Validation des schémas EBA
      - Rapport de conformité et anomalies détectées
    """

    def __init__(self):
        super().__init__(
            name="CorepAgent",
            description=(
                "Agent Expert COREP : génère et valide des rapports COREP "
                "selon les spécifications EBA (ratios, données prudentielles, schémas XML/CSV)."
            ),
            llm=LLM(model="gpt-4-turbo"),
            memory=True,
            tools=[
                Tool.Calculator,   # pour effectuer les calculs de ratios
                Tool.FileWriter,   # pour générer les fichiers de reporting
                Tool.FileReader,   # pour relire et valider les schémas
                Tool.WebSearch     # pour consulter la documentation EBA si besoin
            ]
        )

    async def run(self, input_data: str) -> str:
        """
        Exécuté avec :
            await CorepAgent().run(données_métier)

        Paramètre `input_data` :
        - Données d'entrée (ex. portefeuille de crédits, paramètres de risque)

        Produit :
        1. Le reporting COREP au format exigé (XML/CSV)
        2. Un document de validation des règles appliquées
        3. Un rapport d'anomalies (données manquantes, hors norme)
        """
        return await super().run(input_data)

    # **Ajoutez cette méthode pour lever l’abstraction**
    async def step(self):
        """
        Délègue l’exécution d’une étape à la classe de base.
        """
        return await super().step()
