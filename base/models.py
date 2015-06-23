from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    
    # The additional attributes we wish to include.
    father_name = models.CharField(max_length=20, blank=False, default='-Not mentioned-')
    mother_name = models.CharField(max_length=20, blank=False, default='-Not mentioned-')
    website = models.URLField(blank=True)
    mobile = models.PositiveIntegerField(blank=False, default=0000000000)
    picture = models.ImageField(upload_to='profile_images', blank=False, default='no_image.png')
    
    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.picture)
    image_thumb.short_description = 'Thumb'
    image_thumb.allow_tags = True
    
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
        

