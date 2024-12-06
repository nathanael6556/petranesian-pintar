import uuid
import os
import pickle
import shutil
import streamlit as st
from typing import Any


class User:
    _user_storage_path = "./storage/users"
    _user_info_file = "user_info.pkl"

    uid: str
    name: str

    # en | id
    language: str
    extra_data: Any

    def __init__(self, uid: str | None):
        self.name = "Unknown"
        self.language = "en"
        self.extra_data = None

        if uid is not None:
            self.uid = uid
            # Check if the user directory exists, if not then create it
            if not os.path.exists(self.get_base_path()):
                os.makedirs(self.get_base_path())

            # Check if the user info file exists, if not then create it
            if not os.path.exists(os.path.join(self.get_base_path(), self._user_info_file)):
                self.save()

            # Load the user info from the file
            with open(os.path.join(self.get_base_path(), self._user_info_file), "rb") as f:
                self.__dict__ = pickle.load(f)

    def get_preferred_language_string(self):
        if self.language == "en":
            return "English"
        elif self.language == "id":
            return "Bahasa Indonesia"
        else:
            return "Unknown"

    def get_base_path(self):
        return os.path.join(User._user_storage_path, self.uid)

    def save(self):
        with open(os.path.join(self.get_base_path(), self._user_info_file), "wb") as f:
            # Copy only the dict of the user object
            pickle.dump(self.__dict__, f)

    def delete(self):
        shutil.rmtree(self.get_base_path())

    @staticmethod
    def get_random_uid() -> str:
        return uuid.uuid4().hex

    @staticmethod
    def get_users():
        users = []
        # Test if directory exists, if not then create it
        if not os.path.exists(User._user_storage_path):
            os.makedirs(User._user_storage_path)

        # Iterate over all directories in the user directory
        for user_dir in os.listdir(User._user_storage_path):
            # Check if the directory is a valid user directory
            if os.path.isdir(os.path.join(User._user_storage_path, user_dir)):
                # Load the user info from the file
                with open(os.path.join(User._user_storage_path, user_dir, User._user_info_file), "rb") as f:
                    user = User(uid=None)
                    user.__dict__ = pickle.load(f)

                    # Add the user to the list if it's not the default "Guest" user
                    users.append(user)

        # If there are 0 users, create a default "Guest" user
        if len(users) == 0:
            user = User(uid="guest")
            user.name = "Guest"
            user.language = "English"
            user.save()

            users.append(user)

        return users


def get_st_user() -> User:
    if "user" in st.session_state:
        return st.session_state.user
    raise Exception("User not found")


def auth_check():
    if "user" not in st.session_state:
        st.rerun()