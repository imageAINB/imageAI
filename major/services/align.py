from major.utils.model_utils import align_set
from major.utils.const import Const as const


def align(setname):
    setname = const.TRAIN_SET_PRE + '/' +setname
    in_dir = setname + "/in"
    out_dir = setname + "/out"
    argv = [in_dir, out_dir]
    align_set(argv)
