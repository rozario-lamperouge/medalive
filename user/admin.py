from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Staff, Doctor, Vendor, Post, Media, Patient

class DoctorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.user.groups.filter(name='Staff').exists():
            staff = Staff.objects.get(user=request.user)
            return Doctor.objects.filter(staff=staff)
        else:
            return Doctor.objects.all()

admin.site.register(Staff)
admin.site.register(Vendor)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Post)
admin.site.register(Media)
admin.site.register(Patient)
