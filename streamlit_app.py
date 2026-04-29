import streamlit as st 
from langchain_openai import OpenAI
st.title( ' Aplicación de inicio rápido' ) 

openai_api_key = st.secrets["OPENAI_API_KEY"]
def  generate_response ( input_text ): 
  llm = OpenAI(temperature= 0.7 , openai_api_key=openai_api_key) 
  st.info(llm(input_text)) 
with st.form( 'my_form' ): 
  text = st.text_area( 'Ingrese texto:' , '¿Cuáles son los tres consejos clave para aprender a programar?' ) 
  submitted = st.form_submit_button( 'Enviar' ) 
  if  not openai_api_key.startswith( 'sk-' ): 
    st.warning( '¡Ingrese su clave API de OpenAI!' , icon= '⚠' ) 
  if submitted and openai_api_key.startswith( 'sk-' ): 
    generar_respuesta(texto)
