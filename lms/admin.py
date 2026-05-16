from django.contrib import admin
from .models import Course
from .models import Enrollment

admin.site.register(Course)
admin.site.register(Enrollment)

