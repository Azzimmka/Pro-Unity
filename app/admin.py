from django.contrib import admin
from .models import Registration, Category, Course

admin.site.register(Registration)
admin.site.register(Course)
admin.site.register(Category)

# Register your models here.
