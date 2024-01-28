import streamlit as st 
import google.generativeai as ai
import os
def main():
    st.header("chat bot")
    os.environ['GOOGLE_API_KEY']="AIzaSyAqtRmOxpAqDC1NRV0T-2M2TxQqazgImQ0"
    ai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    model=ai.GenerativeModel('gemini-pro')
    ad=st.text_input("ask your question below");
    question=ad
    if st.button("submit"):
        response=model.generate_content(question)
        st.success(response.text)

if __name__=="__main__":
    main()
