from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse

class CallbackView(View):
    def get(self, request, *args, **kwargs):
        # callbackにアクセスがあった場合にOKを表示
        return HttpResponse('OK')  # 文字列を返すだけなら、テンプレートではなくHTTPレスポンスだけで可能