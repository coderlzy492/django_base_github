from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from book.models import BookInfo, CharacterInfo

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


def create_book(request):

    book = BookInfo.objects.create(
        book_name='QA之道',
        pub_date='2008-05-18',
        read_count=288,
        comment_count=199,
        book_is_delete=0
    )

    return HttpResponse('Done!!')


def shop(request, province_id, city_id):
    """
    shop函数
    :param request:
    :param province_id: 省份
    :param city_id: 城市
    :return:
    """

    query_params = request.GET
    # print(query_params)

    # getlist方法用于一键多值的情况
    header = query_params.getlist('product_name')

    # get方法用于获取单个键的值
    # header = query_params.get('product_name')

    print(f'返回的value:{header}')

    return HttpResponse('新店即将开业,敬请期待~🎉')


def register_mobile(request, phone):

    return HttpResponse('尊敬的用户,您的手机号已在本平台完成注册~🎉')


def register(request):
    """
    postman中模拟传入form-data类型数据
    :param request:
    :return:
    """

    data = request.POST
    print(data)

    return HttpResponse('Return form-data success~')


def register_json(request):
    """
    postman中模拟传入JSON类型数据
    :param request:
    :return:
    """

    body = request.body
    # print(body)

    body_str = body.decode()
    # print(body_str)

    import json
    body_dict = json.loads(body)
    print(body_dict, type(body_dict))

    header = request.META
    # print(header, type(header))

    return HttpResponse('Return JSON success~')


def response(request):
    """
    定义response查看接口响应
    :param request:
    :return: 包含的status字段定义了返回状态码

        1xx:(消息)
        2xx:(成功)
            200:OK
        3xx:(重定向)
        4xx:(请求有问题)
            404:找不到页面   -->路由问题                                                                               路由有问题
            403:禁止访问    -->权限问题
        5xx:(服务器有问题)
    """
    res = HttpResponse('Return response successfully~', status=200)

    # 设置响应头的信息
    res['name'] = 'itcast'

    return res


def response_info(request):

    import json

    info = {
        'Department': 'Lark QA-Video Conference',
        'Email': 'lvzhenyang@bytedance.com',
        'City': 'Shanghai'
    }

    json_none_dict = json.dumps(info)
    print(f'返回数据:{json_none_dict},类型为:{type(json_none_dict)}')
    return JsonResponse(data=json_none_dict, safe=False)


def redirect_url(request):

    return redirect('http://www.itcast.cn/')

# # Method1:insert
# from book.models import BookInfo
# book0 = BookInfo(book_name='射雕英雄传',
#                  pub_date='1985-05-01',
#                  read_count=12,
#                  comment_count=34,
#                  book_is_delete=0)
#
# # Method2:insert
# # objects==>相当于一个代理,帮我们实现增删改查
# BookInfo.objects.create(book_name='Flask',
#                         pub_date='2028-09-01',
#                         read_count=10,
#                         comment_count=0,
#                         book_is_delete=0
# )
#
# # Method1:update
# book1 = BookInfo.objects.get(id=6)
# book1.book_name = 'Requests'
# book1.save()
#
# # Method2:update
# BookInfo.objects.filter(id=6).update(book_name='Scrapy', comment_count=100)
#
# # Method1:delete(物理删除)
# # 删除分为物理删除 & 逻辑删除
# # 物理删除(这条数据记录被删除)
# book1 = BookInfo.objects.get(id=6)
# book1.delete()
#
# BookInfo.objects.get(id=6).delete()
# BookInfo.filter(id=5).delete()
#
# # 逻辑删除(这条数据记录的标记位发生了变更)