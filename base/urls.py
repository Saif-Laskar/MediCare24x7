from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from base import settings

urlpatterns = [

    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include("ambulance.urls")),
    path("appointment/", include("appointment.urls")),
    path("pharmacy/", include("pharmacy_control.urls")),
    path('', include('blood_donation.urls')),
    path('', include('appointment.urls')),
    path('', include('ml_prediction.urls')),
    path('', include('health_records.urls')),
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
