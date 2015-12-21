from django import forms
from blanc_basic_assets.models import Image  # , ImageCategory


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['title', 'file']

    # def __init__(self, *args, **kwargs):
    #     super(ImageForm, self).__init__(self, *args, **kwargs)
    #     self.fields['category'].queryset = ImageCategory.objects.all()


class FileForm(forms.Form):
    file = forms.FileField()
