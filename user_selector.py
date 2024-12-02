import streamlit as st
from users import User

st.title("Petranesian Pintar")
st.markdown("Who is going to use this app?")

c1, c2, c3 = st.columns(3)

# Load all users
users = User.get_users()

# Split users into 3 equal arrays
user1 = [users[i] for i in range(0, len(users), 3)]
user2 = [users[i] for i in range(1, len(users), 3)]
user3 = [users[i] for i in range(2, len(users), 3)]

# Create a button for each user
with c1:
    for user in user1:
        st.button(user.name, type="primary", use_container_width=True, on_click=lambda: select_user(user))

with c2:
    for user in user2:
        st.button(user.name, type="primary", use_container_width=True, on_click=lambda: select_user(user))

with c3:
    for user in user3:
        st.button(user.name, type="primary", use_container_width=True, on_click=lambda: select_user(user))

st.button("New User", type="secondary", on_click=lambda: new_user())
st.button("Delete Users", type="secondary", on_click=lambda: delete_users())

@st.dialog("Create a new user")
def new_user():
    name = st.text_input("Name")
    language = st.radio("Default Language", options={"English": "en", "Indonesia": "id"})
    
    if st.button("Create") and language != None:
        user = User(uid=User.get_random_uid())
        user.name = name
        user.language = language
        user.save()
        
        st.session_state.user = user
        st.rerun()
        
@st.dialog("Delete Users")
def delete_users():
    user_selections = []
    for user in users:
        if st.checkbox(user.name):
            user_selections.append(user)
            
    if st.button("Delete"):
        for user in user_selections:
            user.delete()
            
        st.rerun()

def select_user(user: User):
    st.session_state.user = user