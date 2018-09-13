# coding:utf-8
from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """blog admin"""
    list_display = ('id', 'caption')
