from model.validation import user_validator


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

    def to_tuple(self):
        return self.id, self.name, self.family, self.username, self.password, self.active


