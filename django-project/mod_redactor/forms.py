from django import forms
# from blanc_basic_assets.models import Image  # , ImageCategory


# class ImageForm(forms.ModelForm):
#
#     class Meta:
#         model = Image
#         fields = ['title', 'file']
# def __init__(self, *args, **kwargs):
#     super(ImageForm, self).__init__(self, *args, **kwargs)
#     self.fields['category'].queryset = ImageCategory.objects.all()

# class ImageForm(forms.Form):
#     title = forms.CharField()
#     file = forms.FileField()
#     # category = Image.objects.filter(title='post_upload')
class ImageForm(forms.Form):
    file = forms.ImageField()


class FileForm(forms.Form):
    file = forms.FileField()
