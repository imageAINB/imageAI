from major.utils.const import Const as const
from major.utils.model_utils import classfy_set


def classify(setname):
    setname = const.TRAIN_SET_PRE + '/' + setname
    out_dir = setname + "/out"
    model_path = const.MODEL_PATH
    classify_path = setname +  '/' +const.CLASSFY_SUF
    mode = "TRAIN"
    argv = [mode, out_dir, model_path, classify_path]
    print("out_dir:" + out_dir)
    print("model_path:" + model_path)
    print("classify_path:" + classify_path)
    classfy_set(argv)