from django import forms
from .models import SurveyResponse

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['name', 'thoughts']
        widgets = {
            'thoughts': forms.Textarea(attrs={'rows':3}),
        }
