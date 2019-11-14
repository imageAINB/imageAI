from django.shortcuts import render
from django.http import JsonResponse
from major.services.predict import predict
from major.services.align import align
from major.services.classify import classify
import sys
from major.utils.model_utils import create_set, add_photo
from major.utils.user_utils import create_user_dir
from major.utils.const import Const as const


def index(request):
    if request.method == "POST":
        try:
            state = request.POST.get("state")  # 获取state参数值
            file_obj = request.FILES.get("up_image")  # 获取图片
            username = "admin"      #暂时设定用户为管理员用户
            trainset = "admin_set"  #暂时设定数据集为管理员数据集
            res = JsonResponse({"result": sys.argv[0]})
            print("state:" + state)

            if (state == '1'):  # 暂定state==1为识别
                #create_set("admin_set")
                #create_user_dir("admin")
                res = predict(file_obj = file_obj, username=username, setname=trainset)

            elif(state == '0'):
                align(trainset)
                classify(trainset)

            else:   #暂定0为上传图片
                label = state
                create_set(trainset)
                if add_photo(setname = trainset, file_obj = file_obj, label = label) == False:
                    res = JsonResponse({"result": "上传失败，同名文件已存在"})



        except Exception as e:
            return JsonResponse({"result": "System Error!\n" + repr(e)})

        return res
    return render(request, "index.html")
