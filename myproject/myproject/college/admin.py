from django.contrib import admin
from .models import Student , Course ,Department , Laboratory, Faculty , Visiting_Faculty , Facillities , Contact

# Register your models here.
admin.site.register(Student)

admin.site.register(Course)

admin.site.register(Department)

admin.site.register(Laboratory)

admin.site.register(Faculty)

admin.site.register(Visiting_Faculty)

admin.site.register(Facillities)

admin.site.register(Contact)