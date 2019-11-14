import sys


def save_file(file_obj):
    file_name = "data/test/" + file_obj.name
    f1 = open(file_name, "wb")
    for i in file_obj.chunks():
        f1.write(i)
    f1.close()
    return file_name


def transform_path(path):
    return sys.argv[0] + '/../' + path