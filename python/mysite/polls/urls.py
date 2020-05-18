'''
@Description: URL配置
@Author: Tucw
@Date: 2020-05-18 11:12:45
@LastEditors: Tucw
@LastEditTime: 2020-05-18 15:05:12
'''
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
