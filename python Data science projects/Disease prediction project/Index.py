from asyncio.windows_events import NULL
import Model_deployment as md
import gradio as gr
import pandas as pd
class Symptoms_sample:
    def __init__(self, symptoms,len_symptoms):
        self.symptoms = symptoms
        self.sample=pd.DataFrame()
        print(type(Symptoms))
        sample_dict ={}
        for i in range(1,18):
            if i <= len_symptoms:
                sample_dict["Symptom_"+str(i)]=symptoms[i-1]
            else:
                sample_dict["Symptom_"+str(i)]= NULL 
        self.sample = pd.Series(sample_dict)
        self.sample = pd.DataFrame([sample_dict])
        print(type(self.sample))
        

    def do_prediction(self):
        print(self.sample)
        return md.do_prediction(self.sample)
        


def greet(name):
    s = Symptoms_sample(name,len(name))
    out = s.do_prediction()
    return "Predicted Disease is " + out
def process_selection(selected_items):
    max_selections = 10  # Set your desired maximum here

    if len(selected_items) > max_selections:
        warning = gr.Warning("You can only select a maximum of 10 options.") 
        return gr.update(interactive=False)
    else:
        return gr.update(interactive=True)

with gr.Blocks() as demo:
    gr.Markdown("## Disease prediction")
    with gr.Column():
        Symptoms = gr.CheckboxGroup(choices=['itching', 'skin_rash', 'nodal_skin_eruptions',
       'dischromic _patches',
       'continuous_sneezing', 'shivering', 'chills', 'watering_from_eyes',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'vomiting', 'cough',
       'chest_pain', 'yellowish_skin', 'nausea', 'loss_of_appetite',
       'abdominal_pain', 'yellowing_of_eyes', 'burning_micturition',
       'spotting_ urination', 'passage_of_gases', 'internal_itching',
       'indigestion', 'muscle_wasting', 'patches_in_throat', 'high_fever',
       'extra_marital_contacts', 'fatigue', 'weight_loss', 'restlessness',
       'lethargy', 'irregular_sugar_level',
       'blurred_and_distorted_vision', 'obesity', 'excessive_hunger',
       'increased_appetite', 'polyuria', 'sunken_eyes', 'dehydration',
       'diarrhoea', 'breathlessness', 'family_history', 'mucoid_sputum',
       'headache', 'dizziness', 'loss_of_balance',
       'lack_of_concentration', 'stiff_neck', 'depression',
       'irritability', 'visual_disturbances', 'back_pain',
       'weakness_in_limbs', 'neck_pain', 'weakness_of_one_body_side',
       'altered_sensorium', 'dark_urine', 'sweating', 'muscle_pain',
       'mild_fever', 'swelled_lymph_nodes', 'malaise',
       'red_spots_over_body', 'joint_pain', 'pain_behind_the_eyes',
       'constipation', 'toxic_look_(typhos)', 'belly_pain',
       'yellow_urine', 'receiving_blood_transfusion',
       'receiving_unsterile_injections', 'coma', 'acute_liver_failure',
       'swelling_of_stomach', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload', 'phlegm',
       'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'fast_heart_rate', 'rusty_sputum', 'pain_during_bowel_movements',
       'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
       'cramps', 'bruising', 'swollen_legs', 'swollen_blood_vessels',
       'prominent_veins_on_calf', 'weight_gain', 'cold_hands_and_feets',
       'mood_swings', 'puffy_face_and_eyes', 'enlarged_thyroid',
       'brittle_nails', 'swollen_extremeties', 'muscle_weakness',
       'abnormal_menstruation', 'anxiety', 'slurred_speech',
       'palpitations', 'drying_and_tingling_lips', 'knee_pain',
       'hip_joint_pain', 'swelling_joints', 'painful_walking',
       'movement_stiffness', 'spinning_movements', 'unsteadiness',
       'pus_filled_pimples', 'blackheads', 'scurring',
       'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'skin_peeling', 'silver_like_dusting',
       'small_dents_in_nails', 'inflammatory_nails', 'blister',
       'red_sore_around_nose', 'yellow_crust_ooze'], value=["skin_rash", "itching"], label="Select Symptoms:")
        btn = gr.Button(value="Predict Disease")
    print(Symptoms)  
    Output = gr.Textbox(label="Predicted Disease")

    btn.click(greet, Symptoms,Output)
    Symptoms.change(process_selection, inputs=Symptoms, outputs=btn)
if __name__ == "__main__":
    demo.launch()
 
