from django.contrib import admin
from contents.models import ContentType, Content, ContentPermission, AcademicDuration, CurrentAcademicDuration

admin.site.register(ContentType)
admin.site.register(Content)
admin.site.register(ContentPermission)
admin.site.register(AcademicDuration)
admin.site.register(CurrentAcademicDuration)
