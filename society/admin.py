from django.contrib import admin
from . import models

# Register your models here.
class SocietyMemberInline(admin.TabularInLine):
    model = models.SocietyMember

admin.site.register(models.Society)