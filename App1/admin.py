from django.contrib import admin
from .models import Post, Contact
# Register your models here.

@admin.register(Post)
class Postmodeladmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']


admin.site.register(Contact)