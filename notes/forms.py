from django import forms
from . import models



#Model form for creating new notes
class CreateNote(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title', 'body', 'slug', 'thumb']
