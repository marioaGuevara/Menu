import streamlit as st

c1, c2, c3 = st.columns(3)

with c1:
    with st.expander('Pizza Familiar -- $160 MXN'):
        st.image('./imgs/familiar.png')
        st.write('24 piezas, con pepperoni, queso crema y carne molida.')
    
    with st.expander('Pizza Pepperoni -- $150 MXN'):
        st.image('./imgs/pepperoni.png')
        st.write('12 piezas con sobrecarga de pepperoni.')
    
with c2:
    with st.expander('Pizza Suprema -- $150 MXN'):
        st.image('./imgs/suprema.png')
        st.write('12 piezas, con chile morrón, carne, champiñones y pepperoni.')
    
    with st.expander('Pizza Queso -- $100 MXN'):
        st.image('./imgs/queso.png')

with c3:
    with st.expander('Pizza Manzana -- $100 MXN'):
        st.image('./imgs/manzana.png')
        st.write('12 piezas, con manzana')
    
    with st.expander('Pizza Personal -- $80 MXN'):
        st.image('./imgs/personal.png')
        st.write('4 piezas, pepperoni')

