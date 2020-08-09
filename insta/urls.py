from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home, name ='home'),
    url(r'index/', views.index_test, name='index'),
]