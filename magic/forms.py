from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    #make one of these for each model

    class Meta:
        model = Card
        fields = ('name', 'edition', 'condition', 'language', 'release_date', 'collection')
