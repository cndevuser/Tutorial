'''
@Description: URL配置
@Author: Tucw
@Date: 2020-05-18 11:12:45
@LastEditors: Tucw
@LastEditTime: 2020-05-18 11:14:40
'''
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]
