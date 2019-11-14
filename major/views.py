from django.shortcuts import render
from django.http import JsonResponse
from major.services.predict import predict
# Create your views here.


def index(request):
    if request.method == "POST":
        try:
            state = request.POST.get("state")  # 获取state参数值
            file_obj = request.FILES.get("up_image")  # 获取图片
            print(state)
            if (state == 1 or True):  # 暂定state==1为识别
                model_path = 'data/20180402-114759/20180402-114759.pb'  # 模型路径
                clf_path = 'data/classify/classes.pkl'  # 分类器路径

                res = predict(file_obj, model_path, clf_path)
        except Exception as e:
            return JsonResponse({"result": "System Error!\n" + repr(e)})

        return res
    return render(request, "index.html")
