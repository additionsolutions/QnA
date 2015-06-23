from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Group, Permission
from base.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic.list import ListView


def index(request):
    context = RequestContext(request)
    context_dict = {'message': 'Hello Rahul Shinde'}
    return render_to_response('base/index.html', context_dict, context)


def aboutus(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "This page is about us"}
    return render_to_response('base/aboutus.html', context_dict, context)
    
def excelencia(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "This page is about Excelcia"}
    return render_to_response('base/excelencia.html', context_dict, context)

def register(request):
    redirect_url = request.GET.get('next')
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
             user = user_form.save()
             user.set_password(user.password)
             user.save()
             profile = profile_form.save(commit=False)
             profile.user = user
             if 'picture' in request.FILES:
                 profile.picture = request.FILES['picture']
             profile.save()
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

    return render_to_response('base/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context_instance=RequestContext(request))

    
    
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
        return render(request, 'base/login.html', {})
        
        
# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/base/')
    

def profile(request):
    context = RequestContext(request)
    flag = False
    group = Group.objects.get(name='site_admin')
    users = group.user_set.all()
    for muser in users:
        if muser == request.user:
            flag = True
    context_dict = {'user': request.user, 'admin': flag}
    if flag:
        return render_to_response('base/profile_admin.html', context_dict, context)
    else:
        return render_to_response('base/profile.html', context_dict, context)

        
def phonetics(request):
    context = RequestContext(request)
    flag = False
    group = Group.objects.get(name='site_admin')
    users = group.user_set.all()
    for muser in users:
        if muser == request.user:
            flag = True
    context_dict = {'user': request.user, 'admin': flag}
    if flag:
        return render_to_response('base/profile_admin.html', context_dict, context)
    else:
        return render_to_response('base/phonetics.html', context_dict, context)        
    

def english(request):
    context = RequestContext(request)
    flag = False
    group = Group.objects.get(name='site_admin')
    users = group.user_set.all()
    for muser in users:
        if muser == request.user:
            flag = True
    context_dict = {'user': request.user, 'admin': flag}
    if flag:
        return render_to_response('base/profile_admin.html', context_dict, context)
    else:
        return render_to_response('base/english_test.html', context_dict, context) 
        
def englishtest2(request):
    context = RequestContext(request)
    flag = False
    group = Group.objects.get(name='site_admin')
    users = group.user_set.all()
    for muser in users:
        if muser == request.user:
            flag = True
    context_dict = {'user': request.user, 'admin': flag}
    if flag:
        return render_to_response('base/profile_admin.html', context_dict, context)
    else:
        return render_to_response('base/english_test2.html', context_dict, context) 
        
        
def qna(request):
    context = RequestContext(request)
    context_dict = {'message': 'Tiny Totts'}
    if request.user.is_authenticated():
        return render_to_response('base/qna.html', context_dict, context)
    else:
        return render_to_response('base/qnaguest.html', context_dict, context)


class UserListView(ListView):

    model = User
    template_name = 'base/user_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return context


def userdelete(request, id):
   usr = User.objects.get(pk = id)
   usr.delete()
   return HttpResponse('deleted')

def userupdate(request, id):
   usr = User.objects.get(pk = id)
   usr.save()
   return HttpResponse('Updated')
   
   
def cardgame(request):
    context = RequestContext(request)
    context_dict = {'message': 'Card Game by Rahul Shinde developed with the help of : "http://www.elated.com/articles/drag-and-drop-with-jquery-your-essential-guide/"'}
    return render_to_response('base/cardgame.html', context_dict, context)

def submit_click(request):
    context = RequestContext(request)
    context_dict = {'message': 'move to homepage'}
    #print '----in base view-----'
    return render_to_response('base/profile.html', context_dict, context)
