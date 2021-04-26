from django import forms


class LocationForm(forms.Form):

    where_are_you = (
        forms.CharField()
    )  # widget=forms.TextInput(attrs={"class": "form-control"})
    at_what_time = forms.TimeField(
        widget=forms.TimeInput(attrs={"class": "form-control", "type": "time"})
    )
