from django import forms
from fuel.models import Fuel


class SearchForm(forms.Form):
    fraze = forms.CharField(
        required=False,
#        label="Fraza",
        disabled=False,
        max_length=20,
        min_length=2,
        strip=True,
        empty_value="")


class FuelForm(forms.ModelForm):
    class Meta:
        model = Fuel
        fields = [
            "title",
            "price",
            "date_from",
            "category",
            "image",
            "description",]
        widgets = {
            "date_from": forms.DateInput(attrs={
                "type": "date",
                }),
}
