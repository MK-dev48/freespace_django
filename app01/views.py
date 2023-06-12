from django.shortcuts import render

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