# app/agent/full_orchestrator.py
import asyncio
from app.agent.spec_agent import SpecAgent
from app.agent.arch_agent import ArchAgent
from app.agent.regulatory_agent import RegulatoryExpertAgent
from app.agent.dev_agent import DevAgent
from app.agent.test_agent import TestAgent
from app.agent.aggregator_agent import AggregatorAgent
from app.tool import Tool


async def develop_application(business_need: str):
    # 1. Spécifications fonctionnelles
    print("=== Étape 1 : Spécifications fonctionnelles ===")
    specs = await SpecAgent().run(business_need)
    print(specs, end="\n\n")

    # 2. Architecture technique
    print("=== Étape 2 : Architecture technique ===")
    arch = await ArchAgent().run(specs)
    print(arch, end="\n\n")

    # 3. Validation réglementaire specs/arch
    print("=== Étape 3 : Validation réglementaire des specs et de l’arch ===")
    val1 = await RegulatoryExpertAgent().run(f"Valide ces specs et cette arch :\n{specs}\n{arch}")
    print(val1, end="\n\n")

    # 4. Génération du code
    print("=== Étape 4 : Génération du code source ===")
    code = await DevAgent().run(arch)
    print(code, end="\n\n")

    # 5. Validation réglementaire du code
    print("=== Étape 5 : Validation réglementaire du code ===")
    val2 = await RegulatoryExpertAgent().run(f"Vérifie le code suivant conforme EBA/CRR3 :\n{code}")
    print(val2, end="\n\n")

    # 6. Tests
    print("=== Étape 6 : Génération et exécution des tests ===")
    tests = await TestAgent().run(code)
    print(tests, end="\n\n")

    # 7. Validation réglementaire des résultats de tests
    print("=== Étape 7 : Validation réglementaire des résultats des tests ===")
    val3 = await RegulatoryExpertAgent().run(f"Vérifie les résultats de tests :\n{tests}")
    print(val3, end="\n\n")

    # 8. Agrégation et documentation finale
    print("=== Étape 8 : Agrégation et documentation finale ===")
    docs = await AggregatorAgent().run(
        f"{specs}\n\n{arch}\n\n{code}\n\n{tests}\n\n{val1}\n\n{val2}\n\n{val3}"
    )
    print(docs, end="\n\n")

    # 9. Sauvegarde de la documentation dans un fichier Markdown
    print("=== Étape 9 : Sauvegarde dans 'documentation_finale.md' ===")
    save_code = f"""
with open("documentation_finale.md", "w", encoding="utf-8") as f:
    f.write({docs!r})
"""
    save_result = await Tool.PythonExecute().execute(code=save_code, timeout=10)
    print("Write result:", save_result["observation"], end="\n\n")

    print("=== Processus terminé ===")


if __name__ == "__main__":
    need = input("Décris ton besoin métier : ")
    asyncio.run(develop_application(need))
