from django import forms
from .models import TestSet, TestSetLine
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions

class TestSetForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = True
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-4'
    helper.field_class = 'col-sm-8'
    helper.layout = Layout(
        Field('code', ),
        Field('testname', css_class='input-sm'),
        Field('description', css_class='input-sm'),
        Field('startdate', css_class='input-sm'),
        Field('enddate', css_class='datepicker'),
        FormActions(Submit('/base/registration', 'Submit', css_class='btn-primary'))
    )

    class Meta:
        model = TestSet
	#exclude = ('testset',)
	fields = ('code',
                  'testname',
		  'description',
		  'startdate',
                  'enddate',
		  'groups', )
    
    

class TestSetLineForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = True
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-4'
    helper.field_class = 'col-sm-8'
    helper.layout = Layout(
        Field('filename', ),
        Field('testset', ),
        Field('srno', ),
	Field('name', ),
        Field('description', ),     
        FormActions(Submit('/base/registration', 'Submit', css_class='btn-primary'))

    )
    class Meta:
        model = TestSetLine
        fields = ('filename',
                  'testset',
		  'srno',
		  'name',
                  'description', )
