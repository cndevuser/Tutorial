'''
@Description: 注册可管理模型
@Author: Tucw
@Date: 2020-05-18 11:06:37
@LastEditors: Tucw
@LastEditTime: 2020-05-18 12:06:24
'''
from django.contrib import admin
from .models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
