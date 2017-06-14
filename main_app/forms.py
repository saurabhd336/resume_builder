from django import forms
from django.forms import inlineformset_factory
from .models import Resume

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        exclude = ['user', 'resume_file']

# ProjectFormSet = inlineformset_factory(Resume, Project, fields=('title','detail','start_date','end_date'),max_num=4)