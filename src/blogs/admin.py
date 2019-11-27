from django.contrib import admin
from .models import Blog, Language, Country, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Blog)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(User, UserAdmin)
