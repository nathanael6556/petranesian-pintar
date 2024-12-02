import streamlit as st
from users import auth_check, get_st_user

# Make sure user is specified
auth_check()
user = get_st_user()

with st.form("Modify Profile"):
    name = st.text_input("Name", value=user.name)
    language = st.radio("Default Language", options={"English": "en", "Indonesia": "id"})
    submit = st.form_submit_button("Modify")
    
if submit and language != None:
    user.name = name
    user.language = language
    user.save()