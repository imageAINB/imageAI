from django.http import JsonResponse
from major.utils import file_utils
import contributed.predict as pre
import os


def predict(file_obj, model_path, clf_path):
    file_name = file_utils.save_file(file_obj)
    file_name = file_utils.transform_path(file_name)  # 转化为绝对路径，不然容易找不到文件
    model_path = file_utils.transform_path(model_path)
    clf_path = file_utils.transform_path(clf_path)

    argv = [file_name,
            model_path,
            clf_path]
    name, pos = pre.main(pre.parse_arguments(argv))
    print(name)
    print(pos)
    res = JsonResponse({"result": name,
                        "posibility": pos})
    os.remove(file_name)  # 用完请删除
    return res