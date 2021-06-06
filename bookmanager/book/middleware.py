from django.utils.deprecation import MiddlewareMixin


class TestMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        print('每次请求开始前调用')

    def process_response(self, request, response):
        print('每次响应开始前调用')

        return response
