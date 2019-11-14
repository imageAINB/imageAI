#常量类，用户管理路径常量
class const(object):
    def __init__(self):
        self.__MODEL_PATH = 'data/20180402-114759/20180402-114759.pb'
        self.__TRAIN_SET_PRE = 'data/train_sets'
        self.__USER_PRE = 'data/user'
        self.__CLASSFY_SUF = "classify/classes.pkl"

    @property
    def MODEL_PATH(self):
        return self.__MODEL_PATH

    @property
    def TRAIN_SET_PRE(self):
        return self.__TRAIN_SET_PRE

    @property
    def USER_PRE(self):
        return self.__USER_PRE

    @property
    def CLASSFY_SUF(self):
        return self.__CLASSFY_SUF


Const = const()


