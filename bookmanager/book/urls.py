from django.urls import path
from book.views import index, create_book

urlpatterns = [
    # path(路由, 视图函数)
    path('index/', index),
    path('create/', create_book)
]