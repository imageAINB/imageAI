import contributed.predict as pre
import src.align.align_dataset_mtcnn as align
import src.classifier as classifier
import os
from major.utils.file_utils import save_file
from major.utils.const import Const as const


def predict_photo(argv):
    return pre.main(pre.parse_arguments(argv))


def align_set(argv):
    align.main(align.parse_arguments(argv))


def classfy_set(argv):
    classifier.main(classifier.parse_arguments(argv))


def transform_setname(setname):
    return const.TRAIN_SET_PRE + '/' + setname


def create_set(setname):
    path = transform_setname(setname)
    if os.path.exists(path):
        return False
    os.mkdir(path)
    os.mkdir(path + "/in")
    os.mkdir(path + "/out")
    os.mkdir(path + "/classify")
    return True


def add_photo(setname, file_obj, label):
    path = transform_setname(setname + "/in/" + label)
    if not os.path.exists(path):
        os.makedirs(path)
    return save_file(path, file_obj)

