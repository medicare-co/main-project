from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from MediCare import views

urlpatterns = [
    re_path(r'^$', views.home_redirect, name='home_redirect'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^home/', include('home.urls')),
    re_path(r'^forum/', include('forum.urls')),
    re_path(r'^accounts/profile/$', views.view_profile, name='view_profile'),
    re_path(r'^accounts/profile/edit$', views.edit_profile, name='edit_profile'),
    re_path(r'^accounts/profile/edit_details$', views.edit_details, name='edit_details'),
    re_path(r'^accounts/password/$', views.change_password, name='change_password'),
    re_path(r'^accounts/profile/reset-password/$', PasswordResetView.as_view(template_name='accounts/reset_password.html'), name='reset_password'),
    re_path(r'^accounts/profile/reset-password/done$', PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'), name='password_reset_done'),
    re_path(r'^accounts/view_orders/$', views.view_orders, name='view_orders'),
    re_path(r'^accounts/create_order/$', views.create_order, name='create_order'),
    re_path(r'^accounts/<int:pk>$', views.edit_order, name='edit_order'),
]
