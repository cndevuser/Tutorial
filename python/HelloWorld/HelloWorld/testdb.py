from django.http import HttpResponse
from TestModel.models import demo


def testdb(request):
    test1 = demo(name='mzs')
    test1.save()
    return HttpResponse('数据存储成功')
