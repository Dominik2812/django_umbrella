from django import forms


class LocationForm(forms.Form):

    where_you_wanna_go = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "where you wanna go ?"}
        )
    )
    number_of_days = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "how long ?"}
        )
    )
