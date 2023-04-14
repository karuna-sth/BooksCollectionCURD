from django.urls import path
from . import views

urlpatterns = [
    path('', views.booklist, name='booklist'),
    path('addbook/', views.addbook, name='addbook'),
    path('deletebook/<id>', views.deletebook, name='deletebook'),
    path('editbook/<id>', views.editbook, name='editbook'),
]