import openai
import streamlit as st

def getResponse(post_content):
    openai.api_key=st.secrets["api-keys"]["open_ai"]
    model_engine="text-davinci-003"
    prompt=f"Write an impressive linkedin post about {post_content}"
    max_tokens=1024
    completion=openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer=completion.choices[0].text
    
    return answer

st.write("Welcome to the LinkedIn post generator!")


user_input=st.text_input("Describe your LinkedIn Content: ")

if(st.button("Generate LinkedIn Post")):
    answer=getResponse(user_input)
    st.write(answer)