'''
@Description: 数据模型
@Author: Tucw
@Date: 2020-05-15 17:16:48
@LastEditors: Tucw
@LastEditTime: 2020-05-18 10:46:32
'''
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_cate = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    '''
    @description: 判断是否最新发布
    @param {type} instance
    @return: boolean
    @author: Tucw
    '''

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
