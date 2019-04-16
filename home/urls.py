from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^login/$', LoginView.as_view(template_name='home/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^about/$', views.about, name='about'),
    ]
