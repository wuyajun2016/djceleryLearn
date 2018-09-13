#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog
from .tasks import sendmail
import json
import time


# 方法一（直接发送邮件，会出现5S等待，直到等待完成了才会去执行下面的代码）
# def sendmail(email):
#     print('start send email to %s' % email)
#     time.sleep(5) #休息5秒
#     print('success')
#     return True

def home(request):
    # 耗时任务，发送邮件
    sendmail.delay('test@test.com')  # 方法二：采用异步
    # sendmail('test@test.com')  # 方法一

    # 其他行为
    data = list(Blog.objects.values('caption'))
    return HttpResponse(json.dumps(data), content_type='application/json')
