from django.urls import path
from umbrella_app import views

app_name = "umbrella_app"

urlpatterns = [
    path("", views.LocationFormView.as_view(), name="Location"),
]
