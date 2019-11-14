from django.http import JsonResponse
from major.utils import file_utils
from major.utils.model_utils import predict_photo, create_set
from major.utils.const import Const as const
import os


def predict(file_obj, username, setname):
    userpath = const.USER_PRE + '/' + username
    setpath = const.TRAIN_SET_PRE + '/' +setname
    model_path = const.MODEL_PATH
    clf_path = setpath + '/' + const.CLASSFY_SUF
    file_name = file_utils.save_file(userpath, file_obj)
    print("file_name:")
    print(file_name)
    print("model_path:")
    print(model_path)
    print("clf_path:")
    print(clf_path)
    argv = [file_name,
            model_path,
            clf_path]
    name, pos = predict_photo(argv)
    print(name)
    print(pos)
    res = JsonResponse({"result": name,
                        "posibility": pos})
    os.remove(file_name)  # 用完请删除
    return res

if __name__ == '__main__':
    create_set("test_name")