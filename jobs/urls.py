from django.urls import path
from .views import *

urlpatterns = [

    path('my-postings/', job_list, name='my-postings'),
    path('create/', job_create, name='job-create'),
    path('my-postings/<int:pk>/', job_detail, name='job_detail'),
    path('my-postings/<int:pk>/update/', job_update, name='job_update'),
    path('my-postings/<int:pk>/delete/', job_delete, name='job_delete'),
    path('applications/<int:pk>', ApplicationDetail.as_view(), name='app-detail'),
]