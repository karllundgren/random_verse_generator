from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
#import datetime  # for checking renewal date range.

from django import forms
from .constants import *

class DetermineVolumeForm(forms.Form):
    VOLUME_CHOICES = (
        (allScriptures, allScriptures),
        (oldTestament, oldTestament),
        (newTestament, newTestament),
        (bookOfMormon, bookOfMormon),
        (doctrineAndCovenants, doctrineAndCovenants),
        (pearlOfGreatPrice, pearlOfGreatPrice),

    )
    VOLUME_CHOICES_LIST = [
        allScriptures,
        oldTestament,
        newTestament,
        bookOfMormon,
        doctrineAndCovenants,
        pearlOfGreatPrice,
    ]

    volume = forms.MultipleChoiceField(
        choices = VOLUME_CHOICES,
        #help_text = "Choose the volume of scripture you want a random verse from."
        )

    def clean_volume(self):
        data = self.cleaned_data['volume']
        print(data)
        if data[0] not in self.VOLUME_CHOICES_LIST:
            raise ValidationError(_('Invalid volume of scripture'))
       
        return data