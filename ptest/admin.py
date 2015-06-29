from django.contrib import admin
from ptest.models import TestSet, TestSetLine, Answer,TestQuestion

admin.site.register(TestSet)
admin.site.register(Answer)
admin.site.register(TestSetLine)
admin.site.register(TestQuestion)


