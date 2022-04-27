from django.urls import path

from .views import *
urlpatterns = [
    path('<str:pk>', health_record_home_view, name='health-record-home'),
    path('record/new/', health_record_create_view, name='health-record-create'),
    path('record/<str:pk>/', health_record_detail_view, name='health-record-post-detail'),
    path('record/update/<str:pk>/', health_record_update_view, name='health-record-post-update'),
    path('record/delete/<str:pk>/', health_record_delete_view, name='health-record-post-delete'),
]
