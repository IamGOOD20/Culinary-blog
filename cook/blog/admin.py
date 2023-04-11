from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

# name: Jack
# mail: Jack@gmail.com
# pas: J123123123


class RecipeInLine(admin.StackedInline):
    model = models.Resipe
    extra = 1

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'create_at', 'id']
    inlines = [RecipeInLine]

@admin.register(models.Resipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
# admin.site.register(models.Post, PostAdmin) # if used decorator @admin.register(models.Post)
# admin.site.register(models.Resipe, RecipeAdmin) # if used decorator @admin.register(models.Resipe)
