import streamlit as st
from users import User

def logout():
    if "user" in st.session_state:
        st.session_state.user.save()
        del st.session_state.user
        st.rerun()

if "user" in st.session_state:
    navigation = st.navigation([
        st.Page("main.py", title="Chat"),
        st.Page("user_profile.py", title="User profile"),
        st.Page("user_documents.py", title="My documents"),
        st.Page(logout, title="Log out"),
    ])
else:
    navigation = st.navigation([
        st.Page("user_selector.py", title="User selector"),
    ])

navigation.run()
