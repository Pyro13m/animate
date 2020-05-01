from django import forms
from crispy_forms.helper import FormHelper
from home.models import Review

class ReviewForm(forms.ModelForm):
    # name=forms.CharField(widget=forms.TextInput(
    #     label = 'Name',
    #     required = True,
    #     maxlength = 264,
    # ))
    # review=forms.CharField(widget=forms.Textarea(
    #     label = 'Write your review here...',
    #     required = True,
    # ))

    # def __init__(self, *args, **kwargs):
    #     super(ReviewForm, self).__init__(*args, **kwargs)
    #     helper = self.helper = FormHelper()
    #     layout = helper.layout = Layout()
    #     for field_name, field in self.fields.items():
    #         layout.append(Field(field_name, placeholder=field.label))
    #     helper.form_show_labels = False
    class Meta():
        model=Review
        fields = '__all__'