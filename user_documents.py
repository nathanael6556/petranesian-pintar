import streamlit as st
from users import auth_check, get_st_user
import re
import os

allowed_section_re = re.compile(r'^[a-zA-Z0-9 \-_]+$')

# Make sure user is specified
auth_check()
user = get_st_user()

# This page renders all the documents that the user has created along with their topics.
# Topics are folders that contain the documents, they are stored inside base_path/topics
st.title("My Documents")

@st.dialog("Create new section")
def create_section():
    section_name = st.text_input("Section name", max_chars=32)
    if st.button("Create"):
        if len(section_name) > 0 and allowed_section_re.match(section_name):
            # Create the section directory if does not exist, else error
            if not os.path.exists(os.path.join(user.get_base_path(), "topics", section_name)):
                os.mkdir(os.path.join(user.get_base_path(), "topics", section_name))
            else:
                st.error("Section already exists")
            st.rerun()
        else:
            st.error("Invalid section name. Allowed characters are: a-z, A-Z, 0-9, -, _, and space")

if st.button("Create new section", type="primary"):
    create_section()
    
def get_sections() -> list[str]:
    base_path = user.get_base_path()
    
    # Get all directories in base_path/topics, if does not exist, create it
    if not os.path.exists(os.path.join(base_path, "topics")):
        os.mkdir(os.path.join(base_path, "topics"))
    sections = [d.name for d in os.scandir(os.path.join(base_path, "topics")) if d.is_dir()]
    return sections
    
active_section = st.selectbox("Selected section", get_sections())
uploaded_files = st.file_uploader("Upload files", type=["pdf", "md", "txt", "mp3", "m4a", "wav"], accept_multiple_files=True)