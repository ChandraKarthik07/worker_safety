from django.urls import path
from .views import WorkerList, WorkerDetails ,worker_data

urlpatterns = [
    path('workers/', WorkerList.as_view(), name='worker_list'),
    path('workers/<int:pk>/', WorkerDetails.as_view(), name='worker_details'),
    path('', worker_data, name='worker_data'),

]
