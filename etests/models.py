from django.db import models
from django.contrib.auth.models import User, Group
#from stringfield import StringField

# Defines Test Sets
class TestSet(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=False, null=False)
    testname = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    no_ans = models.IntegerField(default=1, blank=False, null=False) # This to be moved to individual questions
    startdate = models.DateField()
    enddate = models.DateField()
    groups = models.ManyToManyField(Group)
    submit_flag = models.BooleanField(default=False, blank=False, null=False)

    def __unicode__(self):
        return self.code + " - " + self.testname
        
        
# Define Category for Questions e.g. Single line answer, Descriptive answer, option based etc.
class Category(models.Model):
    ANSWER_TYPE_CHOICES = (
        ('RD', 'Radio'),
        ('SL', 'Single Line'),
        ('ML', 'Multiple Lines'),
        ('CK', 'Checkboxes'),
        )
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=250, blank=True, null=True)
    answer_type = models.CharField(max_length=2,
                                      choices=ANSWER_TYPE_CHOICES,
                                      default='SL')

    def __unicode__(self):
        return self.name
        
        
# Define Question - These are the question which learner will answer (sub-questions for TestLines)
class TestQuestion(models.Model):
    #preamble = models.CharField(max_length=200, blank=True, null=True)
    test_question = models.CharField(max_length=500, blank=False, null=False) # Sub Question asked to learner, which learner has to answer
    duration = models.IntegerField(blank=True, null=True) # Time allotted for this question to answer
    tqno_ans = models.IntegerField(blank=False, null=False, default=1) # Number of answers this question has
    tqmarks = models.IntegerField(blank=False, null=False, default=1) # Marks allotted to each answer of this question. In case of option type this mark is overwritten
    category = models.ForeignKey(Category, on_delete=models.PROTECT ,blank=False, null=False)
    url = models.URLField(blank=True, null=True) # For Picture, Audio clip or Video if present

    def __unicode__(self):
        return self.test_question      
               
     
# Defines Test Sets Lines => filename for the test
class TestSetLine(models.Model): # This is Main question which may have many sub questions
    testset = models.ForeignKey(TestSet, on_delete=models.PROTECT)
    filename = models.CharField(max_length=250, blank=True, null=True) # This is present for javascript based questions. When filename is present other question type (question field) is ignored
    srno = models.IntegerField() # Question Number
    name = models.CharField(max_length=100, blank=True, null=True) # Question
    description = models.TextField(blank=True, null=True) # Common Question preamble e.g. Comprehension passage etc.
    question = models.ForeignKey(TestQuestion, on_delete=models.PROTECT, blank=True, null=True) # Link to actual sub questions
    
    class Meta:
        unique_together = (('srno', 'testset'),)
    # unique_together = (('filename', 'testset'), ('srno', 'testset'),)

    def __unicode__(self):
        # return self.testset.code + " - " + self.filename
        if self.filename == '' :
            return self.question.test_question
        else:
            return self.filename
                     
        
# Define Options for each questions if the question type is "Option"
class Option(models.Model):
    t_question = models.ForeignKey(TestQuestion, on_delete=models.PROTECT)
    option = models.CharField(max_length=200, blank=True, null=True)
    srno = models.CharField(max_length=10, blank=False, null=False, default=1)
    mark = models.IntegerField(null=False, blank=False, default=1)
    url = models.URLField(blank=True, null=True) # For Picture, Audio clip or Video if present

    class Meta:
        unique_together = (('t_question', 'srno'),)

    def __unicode__(self):
        if self.option == '':
            return self.url
        else:
            return self.option

            
 
        
# Records answers to Questions in Test Sets Lines
class Answer(models.Model):
    marks = models.IntegerField() # Marks obtained
    #answer = models.TextField(blank=True, null=True) # This will record the answer of the question
    question = models.ForeignKey(TestSetLine, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __unicode__(self):
        return unicode(self.question)


# Define Options for each questions
class Option(models.Model):
    option = models.CharField(max_length=200, blank=True, null=True)
    t_question = models.ForeignKey(TestQuestion, on_delete=models.PROTECT)
    SrNo = models.CharField(max_length=100, blank=False, null=False)
    mark = models.IntegerField( null=False, blank=False)
    url = models.URLField(blank=True, null=True)

    class Meta:
        unique_together = (('t_question', 'SrNo'),)

    def __unicode__(self):
	if self.option == '':
		return self.url
	else:
		return self.option
     
    
