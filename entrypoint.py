import streamlit as st
from session import clear_session
from users import User

def logout():
    if "user" in st.session_state:
        st.session_state.user.save()
        del st.session_state.user
        st.rerun()
        
def start_new_chat():
    if "user" in st.session_state:
        clear_session(st.session_state)
        st.switch_page("main.py")

if "user" in st.session_state:
    navigation = st.navigation([
        st.Page(start_new_chat, title="Start new chat"),
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
