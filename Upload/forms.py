from django import forms
from .models import Upload_files
class Files_Form(forms.ModelForm):
    class Meta:
        model = Upload_files
        fields = [
        'files'
        ]