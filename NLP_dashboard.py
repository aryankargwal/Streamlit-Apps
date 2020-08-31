import streamlit as st

#NLP pkgs
import spacy
from textblob import TextBlob

def text_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)

    tokens = [token.text for token in docx]
    return tokens

def entity_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)

    entities = [(entity.text,entity.label_) for entity in docx.ents]
    return entities


#pkgs


def main():
    """NLP dashboard using Streamlit"""
    st.title("NLP Dashboard using Streamlit")
    st.subheader("Natural Language Processing on Go :)")

    #Tokenization
    if st.checkbox("Show tokens"):
        st.subheader("Enter the sentence you want to tokenize:")
        message = st.text_area("","Type here")
        if st.button("Go"):
            nlp_result = text_analyzer(message)
            st.success(nlp_result)

    #Entity Extractor        
    if st.checkbox("Show entities"):
        st.subheader("Enter the sentence you want to extract entities from:")
        message = st.text_area("","Type here")
        if st.button("Go"):
            nlp_result = entity_analyzer(message)
            st.success(nlp_result)
    
    #Sentiment Analysis
    if st.checkbox("Sentiment Analysis"):
        st.subheader("Enter the sentence you want to extract entities from:")
        message = st.text_area("","Type here")
        if st.button("Go"):
            blob = TextBlob(message)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)



if __name__ == '__main__':
    main()