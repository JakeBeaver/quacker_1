from django.contrib import admin
from app.models import post, authpost, comment
# Register your models here.

admin.site.register(post)
admin.site.register(authpost)
admin.site.register(comment)
