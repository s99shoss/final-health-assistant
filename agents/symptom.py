def analyze_symptoms(symptoms_text):
    # Simple rule-based symptom checker (for demo purposes)
    symptoms = symptoms_text.lower()
    if "fever" in symptoms and "cough" in symptoms:
        return "🤒 You may have flu-like symptoms. Please rest and consider visiting a doctor."
    elif "headache" in symptoms and "nausea" in symptoms:
        return "🤕 These could be signs of migraine. Avoid bright lights and get rest."
    else:
        return "🔍 Your symptoms need further evaluation. Consider consulting a healthcare provider."
