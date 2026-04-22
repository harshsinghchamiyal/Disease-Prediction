import pickle
import pandas as pd

def predict_top_diseases(selected_symptoms):
    model = pickle.load(open("model.pkl", "rb"))
    symptoms_list = pickle.load(open("symptoms.pkl", "rb"))

    input_vector = [1 if s in selected_symptoms else 0 for s in symptoms_list]
    input_df = pd.DataFrame([input_vector], columns=symptoms_list)

    probs = model.predict_proba(input_df)[0]
    diseases = model.classes_

    result = sorted(zip(diseases, probs), key=lambda x: x[1], reverse=True)

    return result[:5]