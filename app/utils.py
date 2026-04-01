def check_emergency(symptoms: str):
    keywords = [
        "chest pain",
        "difficulty breathing",
        "shortness of breath",
        "fainting",
        "unconscious",
        "dizziness"
    ]

    symptoms = symptoms.lower()

    for word in keywords:
        if word in symptoms:
            return True

    return False