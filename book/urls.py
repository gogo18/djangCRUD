from django.urls import path
from . import views
urlpatterns = [
    path('', views.getBook),
    path('form/', views.input),
    path('form/post', views.postBook),
    path('<int:id>/', views.delete ),
    path('edit/<int:id>/', views.edit),
    path('edit/<int:id>/update', views.update)
]