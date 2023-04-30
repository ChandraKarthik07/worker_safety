from django.urls import path
from .views import worker_list, create_worker ,worker_data

urlpatterns = [
    path('workers/', worker_list, name='worker_list'),
    path('workers/<str:pk>/', create_worker, name='create_worker'),
    path('', worker_data, name='worker_data'),

]
