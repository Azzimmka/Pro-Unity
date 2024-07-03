from django.urls import path
from .views import index, register, view_data, card, python, front

urlpatterns = [
    path('', index, name='index'),
    path('card/', card, name='card'),
    path('front/', front, name='front'),
    path('python/', python, name='python'),
    path('register', register, name='register'),
    path('view-data/', view_data, name='view_data'),
]
