from django import forms


class LocationForm(forms.Form):

    Ort = (
        forms.CharField()
    )  # widget=forms.TextInput(attrs={"class": "form-control"})
    Zeit = forms.TimeField(
        widget=forms.TimeInput(attrs={"class": "form-control", "type": "time"})
    )

