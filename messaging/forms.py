from django import forms
from messaging.models import Message
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions

class NewMessageForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = True
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-4'
    helper.field_class = 'col-sm-8'
    helper.layout = Layout(
                Field('to_user',css_class='input-sm' ), 
                Field('short_message',css_class='input-sm'),
                FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))
                )
    class Meta:
        model = Message
        fields = ('short_message',
            'to_user')