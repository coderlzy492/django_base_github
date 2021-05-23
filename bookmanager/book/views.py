from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('OK~')

    """

    :param request:
    :return:
    """
    # 模拟一次数据查询
    context = {
        'name': 'Denver Nuggets'
    }

    return render(request=request,
                  template_name='book/index.html',
                  context=context)
