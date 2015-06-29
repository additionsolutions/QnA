from django.db import models
from django.contrib.auth.models import User, Group

class TestSet(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=False, null=False)
    testsetname = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    startdate = models.DateField()
    enddate = models.DateField()
    groups = models.ManyToManyField(Group, related_name='groups',)
    submit_flag = models.BooleanField(default=False, blank=False, null=False)

    def __unicode__(self):
        return self.code + " - " + self.testsetname


# Defines Test Sets Lines 
class TestSetLine(models.Model): # This is Main question which may have many sub questions
    testset = models.ForeignKey(TestSet, on_delete=models.PROTECT)
    srno = models.IntegerField() # Question Number
    name = models.CharField(max_length=100, blank=True, null=True) # Question
    description = models.TextField(blank=True, null=True) # Common Question preamble e.g. Comprehension passage etc.
    #question = models.ForeignKey(TestQuestion, on_delete=models.PROTECT, blank=True, null=True) # Link to actual sub questions
    
    class Meta:
        unique_together = (('srno', 'testset'),)
    # unique_together = (('filename', 'testset'), ('srno', 'testset'),)

    def __unicode__(self):
            return self.name
            
            
# Define Question - These are the question which learner will answer (sub-questions for TestLines)
class TestQuestion(models.Model):
    testsetline = models.ForeignKey(TestSetLine, on_delete=models.PROTECT)
    srno = models.IntegerField() # Question Number
    name = models.CharField(max_length=500, blank=False, null=False) # Sub Question asked to learner, which learner has to answer
    duration = models.IntegerField(blank=True, null=True) # Time allotted for this question to answer
    marksalloted = models.IntegerField(blank=False, null=False, default=1) # Marks allotted to each answer of this question. In case of option type this mark is overwritten

    class Meta:
        unique_together = (('srno', 'testsetline'),)
        
    def __unicode__(self):
        return self.name 
        
        
# Records answers to Questions in Test Sets Lines
class Answer(models.Model):
    testquestion = models.ForeignKey(TestQuestion, on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT)
    marks = models.IntegerField() # Marks obtained
    answer = models.TextField(blank=True, null=True) # This will record the answer of the question

    def __unicode__(self):
        return unicode(self.testquestion)