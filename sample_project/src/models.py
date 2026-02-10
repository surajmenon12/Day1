"""Database models for the dashboard application."""


class User:
    def __init__(self, user_id, name, email, role="viewer"):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
        }


class Session:
    def __init__(self, session_id, user_id, started_at):
        self.session_id = session_id
        self.user_id = user_id
        self.started_at = started_at
        self.is_active = True

    def end(self):
        self.is_active = False
