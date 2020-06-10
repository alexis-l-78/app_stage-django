from django import forms


class FILM(forms.Form):
    film = forms.CharField(label='Films', max_length=100)

class FormActor(forms.Form):
    actor = forms.CharField(label='Actor', max_length=100)

