from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getLists, name='lists'),
    path('notes/create/', views.createList, name='create-list'),
    path('notes/<str:pk>/delete/', views.deleteNote, name='delete-note'),
    path('notes/<str:pk>/update/', views.updateNote, name='update-note'),
    
    
    path('notes/<str:pk>/', views.getList, name='list'),
]


