import re


def user_validator(user):
    errors = []
    if not (type(user.name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", user.name)):
        errors.append("user Name is Invalid.")

    if not (type(user.family) == str and re.match(r"^[a-zA-Z\s]{3,30}$", user.family)):
        errors.append("user Family is Invalid.")

    if not (type(user.username) == str and re.match(r"^[a-zA-Z\s]{3,30}$", user.username)):
        errors.append("username is Invalid.")

    if not (type(user.password) == str and re.match(r"^[a-zA-Z\s]{3,30}$", user.password > 0)):
        errors.append("Password is Invalid.")
    return errors
