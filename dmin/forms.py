from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User, Group
from base.models import User, UserProfile
from django.core.exceptions import ValidationError
from etests.models import TestSet, TestSetLine ,Answer,Category,TestQuestion,Option
from contents.models import Content, ContentType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions

class GroupForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_tag = True
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-2'
	helper.field_class = 'col-sm-6'
	helper.layout = Layout(
			Field('name',),
			Field('permissions',),
			FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))
			)
	class Meta:
		model = Group
		fields = ('name','permissions')


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	helper = FormHelper()
	helper.form_tag = False
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-2'
	helper.field_class = 'col-sm-4'
	helper.layout = Layout(
			Field('username', css_class='input-sm'),
			Field('first_name', css_class='input-sm'),
			Field('last_name', css_class='input-sm'),
			Field('email', css_class='input-sm'),
			Field('password', css_class='password'),
			Field('confirm_password', css_class='password'),
			Field('groups', css_class='input-sm'),
			#FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))
			)
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password','groups')

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
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-2'
	helper.field_class = 'col-sm-4'
	helper.layout = Layout(
			Field('mother_name', css_class='input-sm'),
			Field('father_name', css_class='input-sm'),
			Field('mobile', css_class='input-sm'),
			Div('picture', css_class='input-sm'),
            #FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))
			#FormActions(Submit('/base/registration', 'Add User', css_class='btn-primary'))
			)

	class Meta:
		model = UserProfile
		fields = ('mother_name', 'father_name', 'mobile', 'picture')

class CategoryForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_tag = True
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-4'
	helper.field_class = 'col-sm-8'
	helper.layout = Layout(
       			Field('name',css_class='input-sm' ),
       			Field('description',css_class='input-sm' ), 
        		FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))

    			)
    	class Meta:
        	model = Category
        	fields = ('name',
          		'description')

class TestQuestionForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_tag = True
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-5'
	helper.field_class = 'col-sm-7'
	helper.layout = Layout(
			Field('test_question', ),
			Field('duration',),
			Field('category'),
			Field('url',),
			FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))
			)

    	class Meta:
        	model = TestQuestion
		fields = ('test_question',
		  	'duration',
			'category',
		  	'url')

class OptionForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_tag = True
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-5'
	helper.field_class = 'col-sm-7'
	helper.layout = Layout(
			Field('option', ),
			Field('t_question', ),
			Field('srno',),
			Field('mark'),
			Field('url',),
			FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))
			)

    	class Meta:
        	model = Option
		fields = ('option',
                  	't_question',
		  	'srno',
			'mark',
		  	'url')
    


class TestSetForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_tag = True
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-5'
	helper.field_class = 'col-sm-7'
	helper.layout = Layout(
			Field('code', ),
			Field('testname', css_class='input-sm'),
			Field('description', css_class='input-sm'),
			Field('no_ans'),
			Field('startdate', css_class='datepicker'),
			Field('enddate', css_class='datepicker'),
			Field('groups', ),
			FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))
			)

    	class Meta:
        	model = TestSet
	#exclude = ('testset',)
		fields = ('code',
                  	'testname',
		  	'description',
			'no_ans',
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
                        Field('question', ),
			Field('name', ),
			Field('description', ),     
			FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))

			)
	class Meta:
		model = TestSetLine
		fields = ('filename',
          		'testset',
	  		'srno',
			'question',
	  		'name',
          		'description', )	
	

class ContentTypeForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_tag = True
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-4'
	helper.field_class = 'col-sm-8'
	helper.layout = Layout(
       			Field('name',css_class='input-sm' ),
       			Field('description',css_class='input-sm' ), 
        		FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))

    			)
    	class Meta:
        	model = ContentType
        	fields = ('name',
          		'description')


class ContentForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_method = 'POST'
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-sm-5'
	helper.field_class = 'col-sm-7'
	helper.layout = Layout(
       			Field('name', ),
       			Field('data', ), 
			Field('createdby',),
			Field('startdate',),
			Field('enddate',),
			Field('picture', ),
       			Field('contenttype', ), 
			Field('groups', ),
        		FormActions(Submit('Submit', 'Submit', css_class='btn-primary'))

    			)
    	class Meta:
        	model = Content
		fields = ('name',
          		'data',
			'createdby',
			'startdate',
			'enddate',
			'picture',
			'contenttype',
			'groups',)
