import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# pandas
# streamlit
# openpyxl
# plotly
# numpy
# matplotlib
# Pillow

# Carga las imágenes

franco = Image.open('images/franco.jpg')

# logo = Image.open('images/logo.png')
# st.sidebar.image(logo, width=180)

# Agrega un título de contexto y una reseña pequeña
st.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 40px; font-weight:bold; text-shadow: 2px 2px 4px #000000;">Contexto</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify;">En la actualidad, llevar el control de las actividades desarrolladas, asi como los fenomenos climatologicos es fundamental.</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: justify;">El objetivo principal es obtener una forma facil de monitorear esto.</p>', unsafe_allow_html=True)
st.markdown("         ")
st.markdown("         ")

col1,col2 = st.sidebar.columns(2)
# col1.image(lluvia, width=90)
# col2.image(paragua, width=94)
st.sidebar.title("Filtros2")

# Agrega el título "Quienes Somos"
st.markdown('<p style="font-family:Calibri Light; color:Black; font-size: 40px; font-weight:bold; text-shadow: 2px 2px 4px #000000;">Quienes Somos</p>', unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)



col1, col2, col3, col4 = st.columns(4) # 



# integrantes

col1.image(franco, width=106)
col1.markdown("[Franco González](https://www.linkedin.com/in/franco-alberto-gonz%C3%A1lez-b1870a22b/)")
# col1.write('Estudiante de Ing. Matemática, UTFSM.')



