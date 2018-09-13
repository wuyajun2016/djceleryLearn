# coding:utf-8
# from __future__ import absolute_import
# from celery.decorators import task  # 原来的,貌似有错,直接换成:from celery.task import task
from celery.task import task
import time
# 定时任务
from celery.schedules import crontab
# from celery.decorators import periodic_task  # 原来的貌似有问题,直接替换成:from celery.task import periodic_task
from celery.task import periodic_task
import datetime


# 异步任务
@task
def sendmail(email):
    print('start send email to %s' % email)
    time.sleep(5)  # 休息5秒
    print('success')
    return True


# 这个貌似没有用到,暂且注释起来
# bind等于True则绑定到celery app对象，可使用app的方法
# @task(bind=True)
# def err_retry(self, email):
#     try:
#         a = 1/0
#     except Exception as e:
#         # 尝试重新执行1次任务
#         raise self.retry(exc=e)


# 每分钟执行一次
# http://docs.celeryproject.org/en/master/userguide/periodic-tasks.html
# 方式一:直接写入一个时间:10s
# @periodic_task(run_every=10)
# 方式二:可以按这种方式设置定时任务开始时间(一般不用这种方式)
# @periodic_task(run_every=datetime.timedelta(hours=1, minutes=15, seconds=40))
# 方式三:crontab()
# @periodic_task(run_every=crontab(hour='13-18'))
@task
# 默认是1min执行一次
# 具体某个值:crontab(minute=15) 即每小时的15分时刻执行一次任务;crontab(minute=0, hour=0)每天零点执行任务;crontab(minute='0,30') 0分和30分执行任务
# 设置范围:crontab(hour='9-12')9-12点每分钟执行一次任务;crontab(hour='9-12,20')9点到12点和20点中每分钟执行任务;
# 设置间隔步长:crontab(minute='*/2')每隔2分钟执行任务;crontab(minute=0, hour='*/3')每3个小时的0分时刻执行1次任务;等等等
# 用到可以参考下:http://yshblog.com/blog/164
def some_task():
    print('periodic task test!!!!!')
    time.sleep(5)
    print('success')
    return True
