from django.shortcuts import render
# http://uguide.ru/tablica-osnovnykh-tegov-html-s-primerami
# Create your views here.
def index(request):
    return render(request, 'index.html')


