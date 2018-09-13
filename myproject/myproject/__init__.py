# coding:utf-8
from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app  # 引入celery对象,就是django运行时加载celery.py文件
import pymysql
pymysql.install_as_MySQLdb()




