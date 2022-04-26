from django.urls import URLPattern, path
from . import views


urlpatterns=[
    path('blood-donation-home', views.blood_donation_home_view, name='blood-donation-home'), # path for home page
    path('post-request', views.post_blood_request_view, name='blood-donation-post-request'), # path for post request
    path('request-detail/<int:pk>', views.blood_request_detail_view, name='blood-donation-request-detail'), # path for request detail
    path('update-request/<int:pk>', views.update_blood_request_view, name='blood-donation-update-request'), # path for update request
]
