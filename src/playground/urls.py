from django.urls import path

from . import views

#URL Config
urlpatterns = [
    path('', views.say_hello, name='home'),
    path('add/', views.add, name='add'),
    path('admin/',views.admin,name="admin")
]