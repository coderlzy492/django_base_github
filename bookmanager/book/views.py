from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
# from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
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


def set_cookies(request):
    """
    第一次请求携带查询内容,
    服务器接收到请求后获取username,
    服务器设置Cookie信息,包括username & password

    浏览器接收到服务器的响应后,保存Cookie
    用户第二次及以后每次访问同样的域名,都会携带Cookie信息来判断用户身份
    :param request:
    :return:
    """

    # 1.获取查询字符串信息
    username = request.GET.get('username')
    password = request.GET.get('password')

    # 2.服务器设置Cookie信息,通过响应对象set_cookie信息
    response = HttpResponse('set_cookies')

    # 3.max_age表示秒数,从响应开始,计数的秒数
    response.set_cookie(key='username', value=username, max_age=60*60)

    return response

    # return HttpResponse('set cookies successfully~')


def get_cookies(request):

    # 1.获取Cookie,字典类型数据
    print(request.COOKIES)

    # 2.获取Cookie中的某个字段信息
    username = request.COOKIES['username']
    # print(username)

    return HttpResponse(username)

    # return HttpResponse('get cookies successfully~')


def set_sessions(request):
    """
    第一次在服务器端设置session信息,服务器会生成一个带有session🆔的Cookie信息
    浏览器接收到该信息后,将Cookie信息保存起来
    第二次及以后每次请求都会携带这个session🆔并做校验,验证无误则执行业务逻辑
    :param request:
    :return:
    """

    # 1.获取username
    user_name = request.GET.get('username')

    # 2.设置session信息
    """
    假设我们通过模型查询得到了用户的信息    
    """
    user_id = 1
    request.session['user_id'] = user_id
    request.session['user_name'] = user_name

    return HttpResponse('set sessions successfully~')


def get_sessions(request):

    user_id = request.session['user_id']
    user_name = request.session['user_name']

    # 在获取字典数据的时候尽量使用get方法,可以减少异常的发生(ousfzv5th4n4xgygxn4h9mq5qlcgc3g5)
    # user_id = request.session.get('user_id')
    # user_name = request.session.get('user_name')

    content = '{},{}'.format(user_id, user_name)

    return HttpResponse(content)


def login(request):

    # print(request.method)
    if request.method == "GET":

        return HttpResponse('GET逻辑~')
    else:
        return HttpResponse('POST逻辑~')


class LoginView(View):
    """
    1.类视图继承自View
    2.类视图中的方法是采用Http方法小写来区分不同的请求方式
    """

    # def get(self, request):
    #
    #     return HttpResponse('GET逻辑~')

    def post(self, request):

        return HttpResponse('POST逻辑~')


# class MyOrderView(View, LoginRequiredMixin):
class MyOrderView(LoginRequiredMixin, View):
    """
    我的订单视图类
    1.已登陆用户---->可以访问
    2.未登陆用户---->无法访问，跳转登陆


    如何定义用户是否登陆??
    我们以登陆后台站点判断是否登陆

    我们这里使用等同于装饰器的另一种方法(多继承)

    Python,C++

    多继承继承多个父类

    LoginRequiredMixin内部会进行用户是否登陆的判断(登陆默认的admin站点)
    1.成功---->显示页面
    2.失败---->返回系统默认的accounts/login/页面


    使用super()可以逐一调用所有的父类方法,并且仅执行一次
    调用顺序遵循MRO类属性顺序
    """

    def get(self, request):

        # islogin是我们模拟了一个标记位
        # islogin = False
        #
        # if not islogin:
        #     return HttpResponse('该用户未登陆,请前往登陆页面')
        # else:
        #     return HttpResponse('get/我的订单页面,这个页面必须登陆')

        return HttpResponse('get/我的订单页面,这个页面必须登陆')

    def post(self, request):

        return HttpResponse('post/我的订单页面,这个页面必须登陆')

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