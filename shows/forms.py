from django import forms
from .models import Show

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = '__all__'
        initial = '__all__'
        description = {'text': forms.Textarea(attrs={"rows":10, "cols":20})}
 
