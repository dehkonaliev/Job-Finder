from django.urls import path
from .views import *

urlpatterns = [

    path('my-postings/', job_list, name='my-postings'),
    path('create/', job_create, name='job-create'),
    path('<int:pk>/', job_detail, name='job_detail'),
    path('<int:pk>/update/', job_update, name='job_update'),
    path('<int:pk>/delete/', job_delete, name='job_delete'),
]