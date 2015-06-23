from django.shortcuts import render, redirect, get_object_or_404, RequestContext, render_to_response
from datetime import datetime, timedelta
from messaging.models import Message
from .forms import NewMessageForm

######################################
# Messages
######################################

def messages(request):
    context = RequestContext(request)
    messages = []
    user = request.user
    current_date = datetime.today() - timedelta(days=7)
    if request.method == 'GET':
        messages = Message.objects.filter(to_user=user, created__gte=current_date).order_by('-created')
        #groups=request.user.groups.all()
    return render_to_response('messaging/messages.html', {'messages': messages }, context)
    
def new_message(request, template_name='dmin/new_message.html'):
    form = NewMessageForm(request.POST or None)
    if form.is_valid():
        frm = form.save(commit=False)
        frm.from_user = request.user
        frm.save()
        return redirect('/a/dmin/profile')
    return render(request, template_name, {'form':form})
