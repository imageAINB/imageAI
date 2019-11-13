from django.shortcuts import render
from django.http import JsonResponse
import contributed.predict as pre
import os
import sys

sys.path.append(os.path.abspath('..'))


# Create your views here.


def index(request):
    if request.method == "POST":
        try:
            state = request.POST.get("state")  # 获取state参数值
            file_obj = request.FILES.get("up_image")  # 获取图片
            if (state == 1 or True):  # 暂定state==1为识别
                print(state)
                file_name = "data/test/" + file_obj.name  # 测试文件保存路径

                f1 = open(file_name, "wb")
                for i in file_obj.chunks():
                    f1.write(i)
                f1.close()

                file_name = sys.argv[0] + '/../' + file_name  # 转化为绝对路径，不然容易找不到文件
                model_path = 'data/20180402-114759/20180402-114759.pb'  # 模型路径
                model_path = sys.argv[0] + '/../' + model_path
                clf_path = 'data/classify/classes.pkl'  # 分类器路径
                clf_path = sys.argv[0] + '/../' + clf_path

                argv = [file_name,
                        model_path,
                        clf_path]
                name, pos = pre.main(pre.parse_arguments(argv))
                print(name)
                print(pos)
                res = JsonResponse({"result": name,
                                    "posibility": pos})
                os.remove(file_name)  # 用完请删除


        except Exception as e:
            return JsonResponse({"result": "System Error!\n" + repr(e)})

        return res
    return render(request, "index.html")
