from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('login',views.login, name = 'login'),
    path('home',views.home, name = 'home'),
    path('add',views.add, name = 'add'),
    path('sub',views.sub, name = 'sub'),
    path('multiply',views.multiply, name = 'multiply'),
    path('divide',views.divide, name = 'divide'),
    path('logout',views.logout, name = 'logout'),
]