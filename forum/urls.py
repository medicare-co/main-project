from django.urls import path, include
from . import views

urlpatterns = [
    path('forum', views.forum, name='forum'),
    path('your_ques', views.your_ques, name='your_ques'),
    path('create_question', views.create_question, name='create_question'),
    path('<int:pk>/', views.view_question, name='view_question'),
    path('<int:pk>/edit', views.edit_question, name='edit_question'),
    ]