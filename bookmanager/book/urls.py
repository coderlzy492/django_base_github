from django.urls import path
from book.views import index, create_book, shop

urlpatterns = [
    # path(路由, 视图函数)
    path('index/', index),
    path('create/', create_book),
    path('<province_id>/<city_id>/', shop)
]