from django.urls import path
from app1 import views

urlpatterns = [

    path('messages/',views.MessageListView.as_view(),name='list'),
    path('messages/create/',views.MessageCreateView.as_view(),name='create'),
]