from django.contrib import admin
from django.urls import path

from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_page, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]