from django.urls import path
from django.urls.converters import register_converter
from book.views import index, create_book, shop, register_mobile, register, register_json, response


# 1.自定义手机号验证转换器
class MobileConverts:
    """
    验证数据的关键:
        正则匹配regex
    """
    regex = '1[0-9]\d{9}'

    # 验证没问题的数据传给视图函数
    def to_python(self, value):
        return int(value)

    # 将匹配结果用于反向解析传值使用
    def to_url(self, value):
        return str(value)


# 2.注册转换器
# converter:转换器类名
# type_name:转换器名字
register_converter(converter=MobileConverts,
                   type_name='mobile')
# 3.

urlpatterns = [
    # path(路由, 视图函数)
    path('index/', index),
    path('create/', create_book),

    # <转换器名字:变量名>
    # 表示转换器,转换器会对变量数据进行正则验证,
    path('<mobile:phone>/', register_mobile),  # <int:province_id>/
    path('<int:province_id>/<int:city_id>', shop),
    path('register/', register),
    path('register_json/', register_json),
    path('response/', response)
]