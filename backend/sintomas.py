def processar_sintomas(sintomas):
    print("\n🔎 Processando sintomas com IA...")
    
    # Aqui entraria o modelo de IA que você deseja usar
    # Por enquanto, apenas um retorno de exemplo
    diagnosticos_exemplo = {
        "Febre": "Infecção viral ou bacteriana",
        "Tosse": "Gripe, resfriado ou infecção respiratória",
        "Dor de cabeça": "Enxaqueca, estresse ou sinusite",
        "Náusea": "Problemas gastrointestinais",
        "Fadiga": "Estresse, falta de sono ou anemia",
        "Dificuldade para respirar": "Asma, COVID-19 ou problemas cardíacos"
    }

    diagnosticos_possiveis = [diagnosticos_exemplo.get(s, "Diagnóstico não encontrado") for s in sintomas]
    
    print("\n🔬 Diagnóstico provável:")
    for sintoma, diagnostico in zip(sintomas, diagnosticos_possiveis):
        print(f"- {sintoma}: {diagnostico}")

    return diagnosticos_possiveis
