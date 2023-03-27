""" Profile URLs """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/orders', views.user_order_history, name='user_order_history'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]
