from django.shortcuts import render
from django.http import JsonResponse
import os
# Create your views here.


def index(request):
    if request.method == "POST":
        file_obj = request.FILES.get("up_image")  # 获取图片
        state = request.POST.get("state")  # 获取state参数值
        print(state)
        file_name = file_obj.name
        f1 = open(file_name, "wb")
        for i in file_obj.chunks():
            f1.write(i)
        f1.close()
        # os.remove(file_name)  # 用完请删除
        return JsonResponse({"result": "hahaha"})
    return render(request, "index.html")
