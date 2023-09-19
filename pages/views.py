from django.shortcuts import render

# Create your views here.

def index(request):
    vares = {'name':'abdo',
              'age':''
              }
    return render(request, template_name='pages\index.html', context=vares)

def aboutus(request):
    return render(request, template_name='pages\Aboutus.html')