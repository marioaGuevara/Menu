import streamlit as st

c1, c2, c3 = st.columns(3)

with c1:
    with st.expander('Espaguetti con Albóndigas -- $120 MXN'):
        st.image('./imgs/spaguetti.png')
        st.write('Espaguetti con albóndigas de carne')
    
with c2:
    with st.expander('Pasta Alfredo -- $120 MXN'):
        st.image('./imgs/alfredo.png')
        st.write('Pasta Alfredo con camarones')

with c3:
    with st.expander('Pasta de Queso -- $120 MXN'):
        st.image('./imgs/pastaqueso.png')
        st.write('Pasta con un shingo de queso')

