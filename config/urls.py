from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("accounts/", include("accounts.urls")),
    path("shops/", include("shops.urls")),
    path("vehicles/", include("vehicles.urls")),
    path("bookings/", include("bookings.urls")),
    path("handovers/", include("handovers.urls")),
    path("rescue/", include("rescue.urls")),
    path("reviews/", include("reviews.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
