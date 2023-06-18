from django.shortcuts import render
from django.views.generic import TemplateView

from .pyapps import sample

# Create your views here.

#ここはDjango公式ドキュメント
from django.http import HttpResponse

def index(request): 
    return HttpResponse("こんにちは。")

#これはDjangoGirlsの
def homepage(request):
    return render(request,  "app01/index.html", {})

def testpage01(request):
    return render(request, "app01/testpage01.html", {})



def ChouseisanMaker(request):
    return render(request, "app01/CM.html", {})

#pyファイルを動かすにはどうやらクラスベースじゃないとだめっぽい？
"""class testpage02(TemplateView):
    template_name = 'app01/testpage02.html'
    
    def get_context_data(self, **kwargs):
        c = sample.sum()
        context = super().get_context_data(**kwargs)
        context['sum'] = c
        return context """

#いや、関数ベースでもいけるっぽいっつーかこっちのほうがシンプルでイカす
def samplepy(request):
    x = sample.sum()
    nya = sample.nyaa()
    context = {
        'sum' : x,
        'neko' : nya,
    }
    return context

def testpage02(request):
    data = samplepy(request)
    return render(request, 'app01/testpage02.html', data)

def testpage03(request):
    return render(request, 'app01/testpage03.html')

#テストページ04
def testpage04(request):
    return render(request, "app01/testpage04.html")