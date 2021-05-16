from django import forms
from django.core.exceptions import ValidationError
import requests
from .secret import api_key
from dataclasses import dataclass


@dataclass
class Forecast:
    umbrella_necessary: bool
    umbrella_days: int
    pullover_necessary: bool
    pullover_days: int
    current_weather: dict


class ForecastAPIError(Exception):
    pass


class LocationForm(forms.Form):
    where_you_wanna_go = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "where you wanna go?",
                "id": "autocomplete",
            }
        )
    )
    number_of_days = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "how many days?",
                "value": 1,
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()

        city = cleaned_data.get("where_you_wanna_go")
        number_of_days = cleaned_data.get("number_of_days")
        # print(self.get_forecast(city, number_of_days))
        try:
            forecast = self.get_forecast(city, number_of_days)
        except ForecastAPIError as e:
            # self.add_error("where_you_wanna_go", error["message"])
            raise ValidationError({"where_you_wanna_go": str(e)})

        cleaned_data["forecast"] = forecast
        return cleaned_data

    def get_forecast(self, city, number_of_days):
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={number_of_days}&aqi=no&alerts=no"
        forecast_response = requests.get(url).json()
        # url = "http://api.weatherapi.com/v1/forecast.json?key={}&q={}&days={}&aqi=no&alerts=no"
        # forecast_response = requests.get(
        #     url.format(api_key, city, number_of_days)
        # ).json()

        # select desired information
        if "error" in forecast_response:
            raise ForecastAPIError(forecast_response["error"]["message"])

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
        return Forecast(
            umbrella_necessary,
            umbrella_days,
            pullover_necessary,
            pullover_days,
            current_weather,
        )
