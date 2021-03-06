from django.contrib import admin
from django.db import models
# from redactor.widgets import AdminRedactorEditor
# from django import forms
# from redactor.widgets import RedactorEditor
# from froala_editor.widgets import FroalaEditor
# , SummernoteInplaceWidget
from django_summernote.widgets import SummernoteInplaceWidget
# from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Recipe, Ingredient, RecipeStep, Header


#  class PostAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         widgets = {
#             'body': RedactorEditor(),
#         }
class RecipeStepInline(admin.TabularInline):
    model = RecipeStep


class IngredientInline(admin.TabularInline):
    model = Ingredient


class RecipeInline(admin.TabularInline):
    model = Post.recipes.through


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    formfield_overrides = {
        models.TextField: {'widget': SummernoteInplaceWidget()},
    }
    inlines = [
        IngredientInline,
        RecipeStepInline,
    ]


class PostAdmin(admin.ModelAdmin):
    """Admin panel class for Post"""
    exclude = ('author',)
    date_hierarchy = 'created_at'
    list_display = ('title', 'author', 'created_at', 'published', 'get_tags')
    list_filter = ['author', 'created_at', 'published']
    search_fields = ('title', 'body')
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {'widget': SummernoteInplaceWidget()},
    }

    inlines = [
        RecipeInline,
    ]

    # http://stackoverflow.com/questions/753704/manipulating-data-in-djangos-admin-panel-on-save
    def save_model(self, request, obj, form, change):
        """Customize save method via admin panel save"""
        if not change:
            obj.author = request.user
        # obj.set_slug()
        obj.save()

    class Media:
        css = {
            'all': ('/static/css/summernote2.css',)
        }

admin.site.register(Ingredient)
admin.site.register(Post, PostAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Header)
