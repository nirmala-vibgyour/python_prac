from django import forms


class ApplicationForm(forms.Form):
    firstName = forms.CharField(max_length=80)
    lastName = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)

