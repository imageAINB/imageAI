import os


def transform_username(username):
    return "data/user/" + username


def create_user_dir(username):
    path = transform_username(username)
    if os.path.exists(path):
        return False
    os.mkdir(path)
    return True
