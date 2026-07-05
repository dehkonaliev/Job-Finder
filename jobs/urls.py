from django.urls import path
from .views import *

urlpatterns = [
  
    path('companies/', company_list, name='company_list'),
    path('companies/create/', company_create, name='company_create'),
    path('companies/<int:pk>/', company_detail, name='company_detail'),
    path('companies/<int:pk>/update/', company_update, name='company_update'),
    path('companies/<int:pk>/delete/', company_delete, name='company_delete'),

    path('jobs/', job_list, name='job_list'),
    path('jobs/create/', job_create, name='job_create'),
    path('jobs/<int:pk>/', job_detail, name='job_detail'),
    path('jobs/<int:pk>/update/', job_update, name='job_update'),
    path('jobs/<int:pk>/delete/', job_delete, name='job_delete'),
]