from django.shortcuts import render, redirect, get_object_or_404, RequestContext, render_to_response
from ptest.models import TestSet, TestSetLine, Answer, TestQuestion
from django.contrib.auth.decorators import login_required
from datetime import date
from contents.models import User
from django.db.models import Q, Max, Min
from .forms import AnswerForm
from django.forms import Textarea, TextInput
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory


######################################
# Exam List for selected group
######################################
def examlist(request):
    context = RequestContext(request)
    examlist = []  
    current_date = date.today()
    if request.method == 'GET':
        examlist = TestSet.objects.filter(groups=request.user.groups.all(),submit_flag=False,startdate__lte=current_date,enddate__gte=current_date)
        
    return render_to_response('ptest/examlist.html', {'examlist': examlist}, context)


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
## Start with first question  
def exam(request, testset):
    testset_obj = TestSet.objects.get(id=testset)
    request.session['testno'] = testset
    request.session['qno'] = 0
    if testset_obj.submit_flag:
        return render(request, 'etests/message.html', { 'message': "Test is already submitted" })
    else:
        return render(request, 'ptest/ptest.html', { 'testset': testset_obj })
        
        
## Navigate   
def examsr(request, action):
        
    # if this is a POST request we need to process the form data
    #AnswerFormSet = formset_factory(AnswerForm, extra=0,)
    #TestSetLineFormSet = inlineformset_factory( TestSetLine, TestQuestion, fields=('srno','name','marksalloted','duration',), extra=0, can_delete=False, widgets={'srno': TextInput(attrs={'size': '2'}), 'name': TextInput(attrs={'size': '120'}), 'duration': TextInput(attrs={'size': '2'}), 'marksalloted': TextInput(attrs={'size': '2'})})
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = AnswerForm(request.POST)
        #formset = TestSetLineFormSet(request.POST, request.FILES, instance=Record_obj[0])
        # check whether it's valid:
        if formset.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form and Navigate
    else:
            # Navigation
        if request.method == 'GET':
            try:
                action = int(action)
            except ValueError:
                raise Http404()
        
            record = "normal"   
            # # Find a First and Last questions
            Record_obj = TestSetLine.objects.filter(testset=request.session['testno'])
            
            # # Calculates the maximum and minimum out of the already-retrieved objects
            last = Record_obj.aggregate(Max('srno'))
            first = Record_obj.aggregate(Min('srno'))   
            
            ### ??? Is this line redundant ??? 
            #obj_testset = TestSet.objects.get(id=request.session['testno'])           
            heading = "Debug this later " #str(obj_testset.testname)
            
            if action == 2: # Next
                sr = request.session['qno'] + 1

            if action == 1: # Previous
                sr = request.session['qno'] - 1

            if action == 0: # Submit
                obj_testset = TestSet.objects.get(id=request.session['testno'])
                obj_testset.submit_flag = True
                obj_testset.save()
                return redirect('/base/profile')
            
            # find out if first or last record
            if sr == last['srno__max']:
                record = "last"
            if sr == first['srno__min']:
                record = "first"
            if last['srno__max'] == first['srno__min']:
                record = "final"
            
            request.session['qno'] = sr
            record_id = sr -1
                  
            question_objs = TestQuestion.objects.filter(testsetline=Record_obj[record_id])
            print "------- Hi ------", question_objs
            #formset = TestSetLineFormSet(instance=Record_obj[record_id])
            return render(request, 'ptest/ptestline.html', { 'testline': Record_obj[record_id],'questions': question_objs,'record':record,})

    #return render(request, 'name.html', {'form': form})
    
    
    
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def grade(request, template_name='ptest/grade.html'):
    #contenttype = ContentType.objects.all()
    usr = User.objects.all()
    test_set = TestSet.objects.all()
    data = {}
    data['object_list'] = usr
    data['test_object_list'] = test_set
    
    return render(request, template_name, data)
    
    
def gradeit(request,usrid,testid):
    if request.method == 'GET':
        try:
            usrid = int(usrid)
            testid = int(testid)
        except ValueError:
            raise Http404()
    
    user_obj = User.objects.get(pk=usrid)
    username = user_obj.get_full_name()
    testset_obj = TestSet.objects.get(pk=testid)
    testset = testset_obj
    #print testset_obj
    testsetline_obj = TestSetLine.objects.filter(testset=testid)
    question_objs = TestQuestion.objects.filter(testsetline=testsetline_obj[0])
    answer_objs = Answer.objects.filter(testquestion=question_objs, user=user_obj)
    #print "------------", answer_objs
    total = 10

    return render(request, 'ptest/gradeit.html', {'user_name':username,'testset_name':testset,'total':total,'testline': testsetline_obj[0],'questions': question_objs,'answers': answer_objs,})
    