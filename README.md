# streamlit-queryparam
💼 Using session state to create sharing URLs

[Tutorial](https://blog.streamlit.io/how-streamlit-uses-streamlit-sharing-contextual-apps/) by Tyler Richards on the streamlit blog.

## 1. Get from URL
```py
params = st.experimental_get_query_params()
```
## 2. Assign params to session state
```py
if "name" not in st.session_state:
    st.session_state["name"] = 'User1'
```
## 3. Set to URL
```py
st.experimental_set_query_params(name=st.session_state["name"])
```


📝 See [app.py](app.py)