class User:
    def __init__(self, user_id, first_name, last_name, email, hashed_password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hashed_password = hashed_password
