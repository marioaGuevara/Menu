import streamlit as st 

c1, c2, c3 = st.columns(3)

with c1:
    with st.expander('Agua de Jamaica -- $20 MXN'):
        st.image('./imgs/jamaica.png')
        st.write('Deliciosa agua de jamaica con refill')

    with st.expander('Agua de Horchata -- $20 MXN'):
        st.image('./imgs/horchata.png')
        st.write('Deliciosa agua de horchata con refill')

with c2:
    with st.expander('Coca Cola --  $20 MXN'):
        st.image('./imgs/coca.png')
        st.write('Refresco sabor cola')
    
    with st.expander('Sprite --  $20 MXN'):
        st.image('./imgs/sprite.png')
        st.write('Refresco sabor lima limón')

with c3:
    with st.expander('Topo Chico -- $25 MXN'):
        st.image('./imgs/topochico.png')
        st.write('Agua Mineral')