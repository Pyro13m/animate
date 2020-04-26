from django import forms
from home.models import Review

class ReviewForm(forms.ModelForm):
    # name=forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class':'form-control',
    #         'placeholder':'Name',
    #     }
    # ))
    # review=forms.CharField(widget=forms.Textarea)
    class Meta():
        model=Review
        fields = '__all__'