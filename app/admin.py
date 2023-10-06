from django.contrib import admin
from .models import Book,CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','image')
    list_display_links = ('id','name','image')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number')
    list_display_links = ('id','phone_number')
