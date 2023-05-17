import spacy
import spacy_streamlit
import streamlit as st
from model_loader import nlp



# nlp = spacy.load("model-best")
image_url = "https://www.partnersineducation.co.uk/wp-content/uploads/2019/03/Assessment-500x500.png"

colors = {"PATHOGEN": "#F67DE3", "MEDICINE": "#7DF6D9", "MEDICALCONDITION": "#a6e22d"}
options = {"colors": colors}

# text = "While bismuth compounds (Pepto-Bismol) decreased the number of bowel movements in those with travelers' diarrhea, they do not decrease the length of illness.[91] Anti-motility agents like loperamide are also effective at reducing the number of stools but not the duration of disease.[8] These agents should be used only if bloody diarrhea is not present."
st.title("Named Entity Recognition")
st.image(image_url, width=300)

text = st.text_area("Enter the text")

if st.button("Submit"):
    if text == "":
        st.write("Please type the text")
    else:
        doc = nlp(text)

        spacy_streamlit.visualize_ner(
            doc,
            show_table=False,
            title="Custom Colors NER Visualization",
            displacy_options={
                "colors": {
                    "PATHOGEN": "#F67DE3",
                    "MEDICINE": "#7DF6D9",
                    "MEDICALCONDITION": "#a6e22d",
                },
                "kb_url_template": "https://www.wikidata.org/wiki/{}",
            },
             key="Custom Colors",
            
        )
