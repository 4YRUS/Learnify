from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('search/<str:word>',views.search, name='search'),
    path('<str:word>',views.search2,name='search2'),
    path('display/',views.display,name='display'),
]