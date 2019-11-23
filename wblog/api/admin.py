from django.contrib import admin
from .models import User, Post
from django.contrib.auth.admin import UserAdmin

from .models import  User

class UserAdmin(admin.ModelAdmin):
     list_display = ('username','email','is_staff','is_admin','is_superuser')
     list_filter = ("username",)

class PostAdmin(admin.ModelAdmin):
     list_display = ('user','id','title','content','timestamp')
     list_filter = ("user",)

admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)