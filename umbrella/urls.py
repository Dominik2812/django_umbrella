from django.contrib import admin
from django.urls import path, include
from umbrella_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.LocationFormView.as_view(), name="index"),
    path("umbrella", include("umbrella_app.urls")),
]
