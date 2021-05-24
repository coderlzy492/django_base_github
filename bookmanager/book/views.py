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