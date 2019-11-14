import os


def save_file(path, file_obj):
    path = path + "/" + file_obj.name
    if os.path.exists(path):
        return False
    f1 = open(path, "wb")
    for i in file_obj.chunks():
        f1.write(i)
    f1.close()
    return path
