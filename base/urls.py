from django.urls import path
from .views import HabitList, HabitDetail, HabitCreate, HabitUpdate, DeleteView, CustomLoginView, RegisterPage, HabitReorder
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

    path('', views.index),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path( 'habit', HabitList.as_view(), name= 'habits'),
    path( 'habit/<int:pk>/', HabitDetail.as_view(), name= 'habit'),
    path( 'habit-create/', HabitCreate.as_view(), name= 'habit-create'),
    path( 'habit-update/<int:pk>/', HabitUpdate.as_view(), name= 'habit-update'),
    path( 'habit-delete/<int:pk>/', DeleteView.as_view(), name= 'habit-delete'),
    path( 'habit-reorder/', HabitReorder.as_view(), name= 'habit-reorder'),
]
