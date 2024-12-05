import os
import pickle
from config import SESSION_SAVED_FIELDS


def save_session(
    session_state,
    saved_fields=SESSION_SAVED_FIELDS,
    filename=None
):
    if filename is None:
        filename = os.path.join(
            session_state.user.get_base_path(),
            "session.pkl"
        )

    selected_session = dict()
    for field in saved_fields:
        if not hasattr(session_state, field):
            continue
        selected_session[field] = getattr(session_state, field)

    with open(filename, "wb") as f:
        pickle.dump(selected_session, f)


def load_session(
    session_state,
    saved_fields=SESSION_SAVED_FIELDS,
    filename=None
):
    if filename is None:
        filename = os.path.join(
            session_state.user.get_base_path(),
            "session.pkl"
        )

    with open(filename, "rb") as f:
        selected_session = pickle.load(f)

    for key, value in selected_session.items():
        setattr(session_state, key, value)