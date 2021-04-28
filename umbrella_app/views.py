from django.views.generic import TemplateView, FormView
from .forms import LocationForm
import requests
from .secrete import apiKey  # , DjangoSecreteKey


class IndexView(TemplateView):
    template_name = "umbrella_app/index.html"


class LocationFormView(FormView):
    template_name = "umbrella_app/index.html"
    form_class = LocationForm

    def form_valid(self, form):
        context = self.get_context_data()
        (
            error,
            umbrella_necessary,
            umbrella_days,
            pullover_necessary,
            pullover_days,
            current_weather,
        ) = self.get_forecast(form)
        context["umbrella_necessary"] = umbrella_necessary
        context["umbrella_days"] = umbrella_days
        context["pullover_necessary"] = pullover_necessary
        context["pullover_days"] = pullover_days
        if error == None:
            context["icon"] = current_weather[0]
            context["temperature"] = current_weather[1]
            context["temperature_felt"] = current_weather[2]
        else:
            context["error"] = error
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["umbrella_necessary"] = None
        return context

    def get_forecast(self, form):
        # retrieve data from the form
        city = form.cleaned_data["where_you_wanna_go"]
        number_of_days = form.cleaned_data["number_of_days"]

        # retrieve weather data from weatherapi.com
        my_API_key = apiKey
        url = "http://api.weatherapi.com/v1/forecast.json?key={}&q={}&days={}&aqi=no&alerts=no"
        forecast_response = requests.get(
            url.format(my_API_key, city, number_of_days)
        ).json()

        # select desired information
        if "error" not in forecast_response.keys():
            error = None
            current_weather = forecast_response["current"]
            current_weather = [
                current_weather["condition"]["icon"],
                int(current_weather["temp_c"]),
                int(current_weather["feelslike_c"]),
            ]

            days = forecast_response["forecast"]["forecastday"]

            umbrella_necessary = False
            umbrella_days = []
            pullover_necessary = False
            pullover_days = []
            for day in days:
                if int(day["day"]["daily_chance_of_rain"]) > 50:
                    umbrella_necessary = True
                    umbrella_days.append(
                        (
                            day["date"],
                            int(
                                day["day"]["daily_chance_of_rain"],
                            ),
                        )
                    )
                if int(day["day"]["mintemp_c"]) < 15:
                    pullover_necessary = True
                    pullover_days.append(
                        (
                            day["date"],
                            int(
                                day["day"]["mintemp_c"],
                            ),
                        )
                    )
            return (
                error,
                umbrella_necessary,
                umbrella_days,
                pullover_necessary,
                pullover_days,
                current_weather,
            )
        else:
            error = forecast_response["error"]
            return error, None, None, None, None, None


#####################################################################################
################## API from openweathermap :
# ################ forcast-API-key does not work,
################## probably due to fees.
#####################################################################################

# def form_valid(self, form):
#     context = self.get_context_data()
#     # get the forecast  from weatherapi.com and calculate whether an umbrella is necessary
#     umbrella_necessary, umbrella_days, current_weather = self.get_forecast(form)
#     context["umbrella_necessary"] = umbrella_necessary
#     context["umbrella_days"] = umbrella_days

#     context["icon"] = current_weather[0]
#     context["temperature"] = current_weather[1]
#     context["temperature_felt"] = current_weather[2]

#     # # get the forecast  from omw.com and calculate whether an umbrella is necessary
#     # error, current_weather = self.get_weather_data_from_owm(form)
#     # if error == False:
#     #     for parameter in current_weather:
#     #         context[parameter] = current_weather[parameter]
#     # else:
#     #     context["error"] = current_weather

#     return self.render_to_response(context)
# def get_weather_data_from_owm(self, form):
#     city = form.cleaned_data["where_you_wanna_go"]
#     my_API_key_current = "e9ab476fc6beabeeb04cba1097a498f5"
#     my_API_key_forecast = "3bbf0887018d6ff4786e9436906e4ee8"

#     url = (
#         "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"
#     )
#     forecast_url = (
#         "http://pro.openweathermap.org/data/2.5/forecast/hourly?q={}&appid={}"
#     )

#     response_for_current = requests.get(url.format(city, my_API_key_current)).json()
#     response_for_forecast = requests.get(
#         forecast_url.format(city, my_API_key_forecast)
#     ).json()

#     if response_for_current["cod"] != "404":
#         error = False
#         current_weather = {
#             "temperature": int(response_for_current["main"]["temp"]),
#             "description": response_for_current["weather"][0]["description"],
#         }
#     else:
#         error = True
#         current_weather = {
#             "Can't retreive weather data: Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."
#         }
#     return error, current_weather
