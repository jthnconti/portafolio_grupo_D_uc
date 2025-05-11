class User:
    def __init__(self, username, email):
        if '@' not in email:
            raise ValueError("Correo inválido.")
        self.username = username
        self.email = email

    def to_dict(self):
        return {"username": self.username, "email": self.email}