from django import forms

from .models import WatchList,ListEntry

class WatchListForm(forms.ModelForm):

    class Meta:
        model = WatchList
        fields = ('title','user',)

