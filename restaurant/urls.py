from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
]
