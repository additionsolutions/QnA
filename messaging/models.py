from django.db import models
from django.contrib.auth.models import User

# Define Message
class Message(models.Model):
    short_message = models.TextField(max_length=250, blank=False, null=False)
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.PROTECT ,blank=False, null=False)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.PROTECT ,blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        show =  (self.created).strftime('%Y-%m-%d , %H:%M') + " >> " + self.short_message
        return show
