import streamlit as st

st.header('`Streamlit-queryparams` 🌐')

# 1. Get params
params = st.experimental_get_query_params()
st.write("Active query params:")
st.write(params)

# 2. Coordinate
# init session variables
if "is_checked" not in st.session_state:
    st.session_state["is_checked"] = (
        params.get("is_checked", ["False"])[0].lower() == "true"
    )

checker = st.checkbox("Checkbox",
                      key="is_checked")

st.write(checker)

st.write(st.session_state["is_checked"])

#3. Set params
st.experimental_set_query_params(is_checked=checker)