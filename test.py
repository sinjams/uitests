import streamlit as st
title = st.text_input('Input a name')
submit = st.button('Submit')
if submit:
    if title.lower() == 'sindhu':
        st.write('Chickoo')
    elif title.lower() == 'maya':
        st.write('Mouse')
    elif title.lower() == 'chickoo':
        st.write('Sindhu')
    elif title.lower() == 'mouse':
        st.write('Maya')
    else: st.write('Swita how could u do this to me')
