import streamlit as st

st.header('`Streamlit-queryparams` 🌐')

params = st.experimental_get_query_params()
st.write("Active query params:")
st.write(params)

