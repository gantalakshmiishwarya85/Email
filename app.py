from hmm import classify
import streamlit as st


st.write("# Email Spam Filtering")
message_text = st.text_input("Enter a message for spam evaluation")
result = classify(message_text)
if st.button("Predict"):
    if result[0] == 'spam' :
        st.error('This message is a Spam', icon="🚨")
    elif result[0] == 'not a spam' :
        st.success('This message is Not a Spam', icon="✅")


