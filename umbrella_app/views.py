from django.views.generic import TemplateView, FormView
from umbrella_app.forms import LocationForm
import requests
# from django.conf.global_settings import google_maps_key
from umbrella.settings import  google_maps_key
# from umbrella_app.secret import api_key, google_maps_key


class IndexView(TemplateView):
    template_name = "umbrella_app/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["umbrella_necessary"] = None
        context["googleMapsAPIKey"] = google_maps_key
        return context


class LocationFormView(FormView):
    template_name = "umbrella_app/index.html"
    form_class = LocationForm

    def form_valid(self, form):
        context = self.get_context_data()

        forecast = form.cleaned_data["forecast"]

        context["umbrella_necessary"] = forecast.umbrella_necessary
        context["umbrella_days"] = forecast.umbrella_days
        context["pullover_necessary"] = forecast.pullover_necessary
        context["pullover_days"] = forecast.pullover_days
        context["icon"] = forecast.current_weather[0]
        context["temperature"] = forecast.current_weather[1]
        context["temperature_felt"] = forecast.current_weather[2]

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["umbrella_necessary"] = None
        context["google_maps_key"] = google_maps_key
        return context
