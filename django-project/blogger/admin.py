from django.contrib import admin
from django.db import models
# from redactor.widgets import AdminRedactorEditor
# from django import forms
# from redactor.widgets import RedactorEditor
# from froala_editor.widgets import FroalaEditor
from django_summernote.widgets import SummernoteInplaceWidget  # , SummernoteInplaceWidget

from .models import Post


#  class PostAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         widgets = {
#             'body': RedactorEditor(),
#         }


class PostAdmin(admin.ModelAdmin):
    """Admin panel class for Post"""
    exclude = ('author',)
    date_hierarchy = 'created_at'
    list_display = ('title', 'author', 'created_at', 'published', 'get_tags')
    list_filter = ['author', 'created_at', 'published']
    search_fields = ('title', 'body')
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        #     models.TextField: {'widget': AdminRedactorEditor},
        models.TextField: {'widget': SummernoteInplaceWidget()},
    }

    # http://stackoverflow.com/questions/753704/manipulating-data-in-djangos-admin-panel-on-save
    def save_model(self, request, obj, form, change):
        """Customize save method via admin panel save"""
        if not change:
            obj.author = request.user
        # obj.set_slug()
        obj.save()


admin.site.register(Post, PostAdmin)
