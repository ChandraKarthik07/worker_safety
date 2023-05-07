from django.urls import path
from .views import worker_list, create_worker ,worker_data,company
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('workers/', worker_list, name='worker_list'),
    path('workers/<str:pk>/', create_worker.as_view(), name='create_worker'),
    path('', worker_data, name='worker_data'),
    path('company/', company.as_view(),name='company')
]
rlpatterns = format_suffix_patterns(urlpatterns)