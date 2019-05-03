from django.contrib import admin
from django.contrib.auth import get_user_model
from pinkcard.models import *

# Register your models here.
#User = get_user_model()

admin.site.register(Student)
admin.site.register(DegreeProg)
admin.site.register(RequestMessage)