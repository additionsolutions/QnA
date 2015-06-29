from django.db import models
from django.contrib.auth.models import User, Group
#from datetime import datetime
#from django.utils import timezone


# Academic duration defines the academic year or semester
class AcademicDuration(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    startdate = models.DateField(blank=False, null=False)
    enddate = models.DateField(blank=False, null=False)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name


# Defines current academic year /semester
class CurrentAcademicDuration(models.Model):
    current = models.ForeignKey(AcademicDuration, blank=False, null=False)

    def __unicode__(self):
        return self.current


# Content Type model to define different types of content available. e.g. Portion, Notice, Photos, Videos etc.
class ContentType(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=250, blank=True)
    
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name

# Content model is where actual contents are stored.
class Content(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    created = models.DateTimeField(auto_now=True)
    createdby = models.ForeignKey(User)
    data = models.TextField(blank=True)
    startdate = models.DateField( blank=False, null=False)
    enddate = models.DateField( blank=False, null=False)
    picture = models.ImageField(upload_to='content_photo', blank=True)
    video = models.URLField(blank=True)
    contenttype = models.ForeignKey(ContentType,on_delete=models.PROTECT)
    groups = models.ManyToManyField(Group)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name



# Content permissions. For Groups and Academic Duration
class ContentPermission(models.Model):
    content = models.ForeignKey(Content)
    group = models.ForeignKey(Group)
    academicduration = models.ForeignKey(AcademicDuration)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return ' '.join([
            self.content,
            self.group,
            self.academicduration,
        ])
