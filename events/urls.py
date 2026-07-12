from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('create/', views.create_event, name='create_event'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('register/<int:pk>/', views.register_event, name='register_event'),
]