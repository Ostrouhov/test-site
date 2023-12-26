from django import forms

class YearForm(forms.Form):
    year = forms.CharField(label='Year greater than: ', max_length=100)