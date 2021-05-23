from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('OK~')

    """
    templates_name: 模板文件名
    context:        视图中的数据传递给模板

    templates/book/index.html中采用{{变量名}}的形式来接收并展示数据
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
