from django.shortcuts import render
from .models import Login
from .forms import LoginForm
# Create your views here.

def index(request):
    vares = {'name':'abdo',
              'age':''
              }
    return render(request, template_name='pages\index.html', context=vares)

def aboutus(request):
    if request.method == 'POST':
        data = LoginForm(request.POST) # like this i do not need to get every single field i want to register
        if data.is_valid():
            data.save()
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     data = Login(username= username, password= password)
    #     data.save()
    return render(request, template_name='pages\Aboutus.html', context={'lf':LoginForm})