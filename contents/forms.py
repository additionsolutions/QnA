from django import forms
from django.forms import ModelForm
from contents.models import AcademicDuration, CurrentAcademicDuration, ContentType, Content, ContentPermission
from django.forms.models import inlineformset_factory


# class ContentTypeForm(forms.ModelForm):
#     name = forms.CharField(max_length=50, help_text="Please enter the Content Type. e.g. 'Portion', 'Notice', 'Photographs' etc.")
#     description = forms.CharField(max_length=250)
#     #slug = forms.CharField(widget=forms.HiddenInput(), required=False)
#
#     # An inline class to provide additional information on the form.
#     class Meta:
#         # Provide an association between the ModelForm and a model
#         model = ContentType
#         fields = ('name', 'description',)


