from django.contrib import admin
from . import models

# Register your models here.

# name: Jack
# mail: Jack@gmail.com
# pas: J123123123

admin.site.register(models.Post)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Resipe)
admin.site.register(models.Comment)
