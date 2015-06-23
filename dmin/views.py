from django.shortcuts import render, render_to_response , redirect, get_object_or_404
from django.views import generic
from django.template import RequestContext
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import ModelForm, ModelChoiceField, HiddenInput
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from base.models import UserProfile
#from base.forms import UserForm, UserProfileForm
from contents.models import Content, ContentType
from etests.models import TestSet, TestSetLine, Answer, Category, TestQuestion, Option
from django.views.generic.list import ListView
from .forms import GroupForm, TestSetForm, TestSetLineForm, ContentTypeForm, ContentForm, UserForm, UserProfileForm, CategoryForm, TestQuestionForm, OptionForm
from django.db.models import ProtectedError
from django.db.models import Count, Sum, Avg


# Create your views here.

def basic(request, template_name='dmin/basic.html'):
    #contenttype = ContentType.objects.all()
    data = {}
    data['object_list'] = " " #contenttype
    return render(request, template_name, data)
    

def register(request):
    redirect_url = request.GET.get('next')
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
             user = user_form.save()
             user.set_password(user.password)
                          
             UserProfile = profile_form.save(commit=False)
             UserProfile.user=user
             if 'picture' in request.FILES:
                UserProfile.picture = request.FILES['picture']

             #user.save()   
             UserProfile.save()
             registered = True
        else:
             print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

#     return render(request,
#             'base/register.html',
#             {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


    if redirect_url is not None:
        user_form.helper.form_action = reversed('submit_survey') + '?next=' + redirect_url

    return render_to_response('dmin/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context_instance=RequestContext(request))


#class UserListView(ListView):

    #model = User
    #template_name = 'dmin/userlist.html'
    
    #def get_context_data(self, **kwargs):
        #context = super(UserListView, self).get_context_data(**kwargs)
        #return context

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def user_list(request, template_name='dmin/userlist.html'):
    userlist = User.objects.all()   
    data = {}
    data['object_list'] = userlist    
    return render(request, template_name, data)

def user_update(request, pk, template_name='dmin/user_form.html'):
    usr = get_object_or_404(User, pk=pk)
    usr_profile = get_object_or_404(UserProfile, user=pk)
    user_form = UserForm(request.POST or None, request.FILES or None, instance=usr)
    profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=usr_profile)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save()
        userprofile = profile_form.save(commit=False)
        userprofile.picture = request.FILES['picture']
        #UserProfile.user=user
        #user.set_password(user.password)
        userprofile.save()
        return redirect('userlist')
    return render(request, template_name, {'user_form':user_form, 'profile_form':profile_form})

def user_delete(request, pk, template_name='dmin/user_form_delete.html'):
    usr = get_object_or_404(User, pk=pk)
    if request.method=='POST':
        usr.delete()
        return redirect('userlist')
    return render(request, template_name, {'object':usr})

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                request.session['user'] = request.user.username
                return HttpResponseRedirect('/a/dmin/profile/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Tiny Totts account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'etests/message.html', { 'message': "Invalid login" })

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'dmin/login.html', {})


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/a/dmin/login')


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def profile(request):
    context = RequestContext(request)
    flag = False
    group = Group.objects.get(name='site_admin')
    users = group.user_set.all()
    userprofile = UserProfile.objects.get(user=request.user)
    for muser in users:
        if muser == request.user:
            flag = True
    context_dict = {'user': request.user, 'userprofile': userprofile, 'admin': flag}
    if flag:
        return render_to_response('dmin/profile_admin.html', context_dict, context)
    else:
        return render_to_response('base/profile.html', context_dict, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def group_list(request, template_name='dmin/group_list.html'):
    grouplist = Group.objects.all()   
    data = {}
    data['object_list'] = grouplist    
    return render(request, template_name, data)

def group_create(request, template_name='dmin/group_form.html'):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('group_list')
    return render(request, template_name, {'form':form})

def group_update(request, pk, template_name='dmin/group_form.html'):
    grouplist = get_object_or_404(Group, pk=pk)
    form = GroupForm(request.POST or None, instance=grouplist)
    if form.is_valid():
        form.save()
        return redirect('group_list')
    return render(request, template_name, {'form':form})


def group_delete(request, pk, template_name='dmin/group_form_delete.html'):
    grouplist = get_object_or_404(Group, pk=pk)
    if request.method=='POST':
        grouplist.delete()
        return redirect('group_list')
    return render(request, template_name, {'object':grouplist})


######################################
# Content Type
######################################

#class ContentTypeForm(ModelForm):

#    class Meta:
#        model = ContentType
#        fields = ('name',
#          'description')

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def contenttype_list(request, template_name='dmin/contenttype_list.html'):
    contenttype = ContentType.objects.all()
    data = {}
    data['object_list'] = contenttype
    return render(request, template_name, data)

def contenttype_create(request, template_name='dmin/contenttype_form.html'):
    form = ContentTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contenttype_list')
    return render(request, template_name, {'form':form})

def contenttype_update(request, pk, template_name='dmin/contenttype_form.html'):
    contenttype = get_object_or_404(ContentType, pk=pk)
    form = ContentTypeForm(request.POST or None, instance=contenttype)
    if form.is_valid():
        form.save()
        return redirect('contenttype_list')
    return render(request, template_name, {'form':form})


def contenttype_delete(request, pk, template_name='dmin/contenttype_form_delete.html'):
    contenttype = get_object_or_404(ContentType, pk=pk)
    if request.method=='POST':
        try:
            contenttype.delete()
        except ProtectedError:
            raise Exception("Field can not be deleted")
        return redirect('contenttype_list')
    return render(request, template_name, {'object':contenttype})

######################################
# Content
######################################

#class ContentForm(ModelForm):

#    class Meta:
#        model = Content
#	exclude = ('video',)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def content_list(request, template_name='dmin/content_list.html'):
    content = Content.objects.all()
    data = {}
    data['object_list'] = content
    return render(request, template_name, data)

def content_create(request, template_name='dmin/content_form.html'):
    form = ContentForm(request.POST or None, initial={'createdby': request.user})
    form.fields['createdby'] = ModelChoiceField(label="", widget=HiddenInput(attrs={'value':request.user}), queryset=User.objects.all())
    if form.is_valid():
        form.save()
        return redirect('getcontentfromcontettype')
    return render(request, template_name, {'form':form})


def content_update(request, pk, template_name='dmin/content_form.html'):
    content = get_object_or_404(Content, pk=pk)
    form = ContentForm(request.POST or None, instance=content)
    if form.is_valid():
        form.save()
        return redirect('getcontentfromcontettype')
    return render(request, template_name, {'form':form})


def content_delete(request, pk, template_name='dmin/content_form_delete.html'):
    content = get_object_or_404(Content, pk=pk)
    if request.method=='POST':        
	content.delete()
        return redirect('getcontentfromcontettype')
    return render(request, template_name, {'object':content})

def getcontentfromcontettype(request, template_name='dmin/content.html'):
    #contenttype = ContentType.objects.all()
    content_typ = ContentType.objects.all()
    data = {}
    data['contenttype_object_list'] = content_typ
    
    return render(request, template_name, data)

def get_content(request,ctype_id):
    if request.method == 'GET':
	try:
            ctype_id = int(ctype_id)
	    
        except ValueError:
            raise Http404()
    
    content_obj = Content.objects.filter(contenttype=ctype_id)
    
	
    return render(request, 'dmin/subpart_content.html', { 'object': content_obj})



######################################
# Test Set for Admin
######################################

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def testset(request, template_name='dmin/testset_list.html'):
    testset = TestSet.objects.all()
    data = {}
    data['object_list'] = testset
    return render(request, template_name, data)

def testset_create(request, template_name='dmin/testset_form.html'):
    form = TestSetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('testset')
    return render(request, template_name, {'form':form})

def testset_update(request, pk, template_name='dmin/testset_form.html'):
    testset = get_object_or_404(TestSet, pk=pk)
    form = TestSetForm(request.POST or None, instance=testset)
    if form.is_valid():
        form.save()
        return redirect('testset')
    return render(request, template_name, {'form':form})

def testset_delete(request, pk, template_name='dmin/testset_form_delete.html'):
    testset = get_object_or_404(TestSet, pk=pk)
    if request.method=='POST':
        testset.delete()
        return redirect('testset')
    return render(request, template_name, {'object':testset})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')    
def testq(request, template_name='dmin/testquestion_list.html'):
    testset_obj = TestSet.objects.all()
    testsetline = TestSetLine.objects.filter(testset=testset_obj)
    data = {}
    data['object_list'] = testsetline
    return render(request, template_name, data)

def testsetline_create(request, template_name='dmin/testsetline_form.html'):
    form = TestSetLineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gettestsetlinefromtestset')
    return render(request, template_name, {'form':form})


def testsetline_update(request, pk, template_name='dmin/testsetline_form.html'):
    testsetline = get_object_or_404(TestSetLine, pk=pk)
    form = TestSetLineForm(request.POST or None, instance=testsetline)
    if form.is_valid():
        form.save()
        return redirect('gettestsetlinefromtestset')
    return render(request, template_name, {'form':form})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def gettestsetlinefromtestset(request, template_name='dmin/testsetline_list.html'):
    #contenttype = ContentType.objects.all()
    test_set = TestSet.objects.all()
    data = {}
    data['test_object_list'] = test_set
    
    return render(request, template_name, data)

def get_testsetline(request,testid):
    if request.method == 'GET':
	try:
            testid = int(testid)
	    
        except ValueError:
            raise Http404()
    
    testsetline_obj = TestSetLine.objects.filter(testset=testid)

    return render(request, 'dmin/subpart_testsetline.html', { 'object': testsetline_obj})

def report_marks(request, template_name='dmin/mark_list.html'):
    answer = Answer.objects.all()
    data = {}
    data['object_list'] = answer
    return render(request, template_name, data)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def report_userwisemarks(request, template_name='dmin/user_report.html'):
    #contenttype = ContentType.objects.all()
    usr = User.objects.all()
    test_set = TestSet.objects.all()
    data = {}
    data['object_list'] = usr
    data['test_object_list'] = test_set
    
    return render(request, template_name, data)

def get_scorecard(request,usrid,testid):
    #print '---in function---'

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
    marks_obj = Answer.objects.filter(user=usrid,question=testsetline_obj)
    
    total = 0
    for obj in marks_obj:
        score = obj.marks
        total = total + score 

    return render(request, 'dmin/score_card.html', {'user_name':username,'testset_name':testset,'object': marks_obj,'total':total})


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def category_list(request, template_name='dmin/category_list.html'):
    categorylist = Category.objects.all()   
    data = {}
    data['object_list'] = categorylist
    return render(request, template_name, data)

def category_create(request, template_name='dmin/category_form.html'):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, template_name, {'form':form})

def category_update(request, pk, template_name='dmin/category_form.html'):
    categorylist = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=categorylist)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, template_name, {'form':form})


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def question_list(request, template_name='dmin/question_list.html'):
    questionlist = TestQuestion.objects.all()   
    data = {}
    data['object_list'] = questionlist
    return render(request, template_name, data)

def question_create(request, template_name='dmin/question_form.html'):
    form = TestQuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render(request, template_name, {'form':form})

def question_update(request, pk, template_name='dmin/question_form.html'):
    questionlist = get_object_or_404(TestQuestion, pk=pk)
    form = TestQuestionForm(request.POST or None, instance=questionlist)
    if form.is_valid():
        form.save()
        return redirect('question_list')
    return render(request, template_name, {'form':form})


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def option_list(request, template_name='dmin/option_list.html'):
    questionlist = TestQuestion.objects.all()
    data = {}
    data['question_object_list'] = questionlist   
    return render(request, template_name, data)


def radio_test(request,template_name='dmin/radio_test.html'):
    questionlist = TestQuestion.objects.all()
    optionlist = Option.objects.all()
    data = {}
    data['object_list'] = optionlist
    data['object'] = questionlist
    return render(request, template_name,data)

def get_option(request,question_id):
    if request.method == 'GET':
	try:
            question_id = int(question_id)
        except ValueError:
            raise Http404()
    
    option_obj = Option.objects.filter(t_question=question_id)

    return render(request, 'dmin/subpart_option.html', { 'object': option_obj})

def option_create(request, template_name='dmin/option_form.html'):
    form = OptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('option_list')
    return render(request, template_name, {'form':form})

def option_update(request, pk, template_name='dmin/option_form.html'):
    optionlist = get_object_or_404(Option, pk=pk)
    form = OptionForm(request.POST or None, instance=optionlist)
    if form.is_valid():
        form.save()
        return redirect('option_list')
    return render(request, template_name, {'form':form})

def option_delete(request, pk, template_name='dmin/option_form_delete.html'):
    option = get_object_or_404(Option, pk=pk)
    if request.method=='POST':
        option.delete()
        return redirect('option_list')
    return render(request, template_name, {'object':option})


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/a/dmin/login')
def userwise_summaryreport(request, template_name='dmin/marks_summary_report.html'):
    #contenttype = ContentType.objects.all()
    usr = User.objects.all()
    data = {}
    data['object_list'] = usr
    
    return render(request, template_name, data)

def get_summaryreport(request,usrid):
    
    if request.method == 'GET':
        try:
            usrid = int(usrid)
        except ValueError:
            raise Http404()
            
    user_obj = User.objects.get(pk=usrid)
    username = user_obj.get_full_name()
    group_objs = Group.objects.filter(user=User.objects.filter(pk=usrid))
    marks_objs = TestSet.objects.filter(groups=group_objs).annotate(marks_total=Sum('testsetline__answer__marks')).order_by('-startdate')
    return render(request, 'dmin/subpart_summary_report.html', {'user_name':username,'testset_objs':marks_objs})


