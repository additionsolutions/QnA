from django import forms
from django.contrib.auth.models import User, Group
from base.models import User, UserProfile
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (PrependedText,  PrependedAppendedText, FormActions, StrictButton)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_tag = False
    #helper.form_method = 'POST'
    #helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('username', css_class='input-sm'),
        Field('first_name', css_class='input-sm'),
        Field('last_name', css_class='input-sm'),
        Field('email', css_class='input-sm'),
        Field('password', css_class='password'),
        Field('confirm_password', css_class='password'),
        #FormActions(Submit('/base/registration', 'Add User', css_class='btn-primary'))
    )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):

        if (self.cleaned_data.get('password') !=
            self.cleaned_data.get('confirm_password')):

            raise ValidationError(
                "Passwords must match."
            )

        return self.cleaned_data


class UserProfileForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    #helper.form_method = 'POST'
    #helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('website', css_class='url'),
        Field('picture', css_class='file'),
        Field('mobile', css_class='input-sm'),
        #FormActions(Submit('/base/registration', 'Add User', css_class='btn-primary'))
    )

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')