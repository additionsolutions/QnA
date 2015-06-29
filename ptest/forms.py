from django import forms
from ptest.models import Answer
from django.forms.formsets import formset_factory

class AnswerForm(forms.ModelForm):
    testquestion = forms.CharField(label='Question', max_length=150)
    answer = forms.CharField(label='Ans:', widget=forms.Textarea)
    #marks = forms.InteField(label='Marks')
    
    class Meta:
        model = Answer
        fields = ('testquestion','answer')
    
#AnswerFormSet = formset_factory(AnswerForm)
# AnswerFormSet = modelformset_factory(
     # Answer, fields=('testquestion', 'answer'),
     # widgets={'answer': Textarea(attrs={'cols': 80, 'rows': 5})})