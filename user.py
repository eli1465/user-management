from validation import user_validator


class User:
    def __init__(self, id, name, family, username, password, active=True):
        self.id = id
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.active = active

    def save(self):
        print (f"{self.id}: {self.name} {self.family} ({'Active' if self.active else 'Inactive'})saved")


    def validate(self):
        return user_validator(self)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "family": self.family,
            "username": self.username,
            "password": self.password,
            "active": self.active
        }