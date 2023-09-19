from django.urls import path
#to Import views and link them with urls
from . import views


urlpatterns = [
    # name parameter is to be able to acll the url in html page using url tag
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus')
]