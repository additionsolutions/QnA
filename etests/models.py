from django.db import models
from django.contrib.auth.models import User, Group
#from stringfield import StringField

# Defines Test Sets
class TestSet(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=False, null=False)
    testname = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    no_ans = models.IntegerField(default=1, blank=False, null=False)
    startdate = models.DateField()
    enddate = models.DateField()
    groups = models.ManyToManyField(Group)
    submit_flag = models.BooleanField(default=False, blank=False, null=False)

    def __unicode__(self):
        return self.code + " - " + self.testname

# Define Category for Questions
class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
	return self.name

# Define Question 
class TestQuestion(models.Model):
    preamble = models.CharField(max_length=200, blank=True, null=True)
    test_question = models.CharField(max_length=500, blank=False, null=False)
    duration = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT ,blank=False, null=False)
    url = models.URLField(blank=True, null=True)

    def __unicode__(self):
	return self.test_question


# Defines Test Sets Lines => filename for the test
class TestSetLine(models.Model):
    filename = models.CharField(max_length=250, blank=True, null=True)
    testset = models.ForeignKey(TestSet, on_delete=models.PROTECT)
    srno = models.IntegerField()
    question = models.ForeignKey(TestQuestion, on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        unique_together = (('srno', 'testset'),)
	# unique_together = (('filename', 'testset'), ('srno', 'testset'),)

    def __unicode__(self):
        # return self.testset.code + " - " + self.filename
	if self.filename == '' :
		return self.question.test_question
	else:
        	return self.filename 
        
# Records answers to Questions in Test Sets Lines
class Answer(models.Model):
    marks = models.IntegerField()
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
     
    
