from django import forms
# from django.forms import Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset
from home.models import Review

class ReviewForm(forms.ModelForm):
    # name=forms.CharField(widget=forms.TextInput(
    #     # label = 'Name',
    #     # required = True,
    #     # maxlength = 264,
    # ))
    # review=forms.CharField(widget=forms.Textarea(
    #     # label = 'Write your review here...',
    #     # required = True,
    # ))

    # def __init__(self, *args, **kwargs):
    #     super(ReviewForm, self).__init__(*args, **kwargs)
    #     self.fields['Review'].label = ''
    #     helper = self.helper = FormHelper()
    #     layout = helper.layout = Layout()
    #     helper[1:2].wrap(Fieldset, "legend of the fieldset")
        # for field_name, field in self.fields.items():
        #     layout.append(Field(field_name, placeholder=field.label))
        # helper.form_show_labels = False
    class Meta():
        model=Review
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'Review': forms.Textarea(attrs={'cols': 50, 'rows': 4, 'placeholder': "Write your review here..."}),
        }