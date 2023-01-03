import streamlit as st 

c1,c2 = st.columns(2)
with c1:

    st.image('imgs/logopizza.png')

with c2:
    st.header('Este es un menú digital')
    st.subheader('Sírvase de ejemplo para hacer menús que funcionen en celulares, por favor.')

st.set_page_config(layout="wide")