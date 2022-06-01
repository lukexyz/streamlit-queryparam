import streamlit as st

st.header('`Streamlit-queryparams` 🌐')

# 1. Get params
params = st.experimental_get_query_params()

# 2. Coordinate
# init session variables
if "is_checked" not in st.session_state:
    st.session_state["is_checked"] = (
        params.get("is_checked", ["False"])[0].lower() == "true"
    )

if "name" not in st.session_state:
    st.session_state["name"] = 'User1'
if params.get("name"):
    st.session_state["name"] = params.get("name")[0]


st.write(f"Hello `{st.session_state['name']}`, these are your URL parameters:")
st.write(params)

checker = st.checkbox("Checkbox", key="is_checked")

st.write('Checked?', st.session_state["is_checked"])

# 3. Set params
st.experimental_set_query_params(is_checked=checker, name=st.session_state["name"])