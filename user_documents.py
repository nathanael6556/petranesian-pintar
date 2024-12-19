import streamlit as st
from documents_manager import clear_all_special_files, get_sections
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
    
active_section = st.selectbox("Selected section", get_sections(user))
uploaded_files = st.file_uploader("Upload files", type=["pdf", "mp3", "m4a", "wav"], accept_multiple_files=True)

if uploaded_files and active_section:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        file_name = uploaded_file.name
        
        final_path = os.path.join(user.get_base_path(), "topics", active_section, file_name)
        with open(final_path, "wb") as f:
            f.write(bytes_data)

@st.fragment
def render_file(file_path: str):
    # Make sure it is a file
    if not os.path.isfile(file_path):
        return
    
    with st.container(border=True):
        col1, col2, col3 = st.columns([8, 2, 1])
        
        file_name = os.path.basename(file_path)
        
        with col1:
            st.markdown(f"{file_name}")
        with col2:
            st.download_button("Download", file_path, file_name, key=file_path+"_download")
            
        with col3:
            if st.button("🗑️", key=file_path+"_delete"):
                os.remove(file_path)
                st.rerun()
            
        # If .md, show the contents
        if file_name.endswith(".md"):
            with st.expander("Show contents"):
                with open(file_path, "r") as f:
                    content = f.read()
                st.markdown(content)
    
if active_section:
    topic_path = os.path.join(user.get_base_path(), "topics", active_section)

    if st.button("Clear all special files"):
        clear_all_special_files(topic_path)
    
    # Show all the files in the section
    files = os.listdir(topic_path)

    for file in files:
        render_file(os.path.join(topic_path, file))