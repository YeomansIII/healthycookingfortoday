from django.core.urlresolvers import reverse, NoReverseMatch
from django.forms import widgets, Media
from django.utils.safestring import mark_safe
from django.conf import settings
import json
from . import PLUGINS, PLUGINS_WITH_CSS


class FroalaEditor(widgets.Textarea):
    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {})
        self.plugins = kwargs.pop('plugins', getattr(settings, 'FROALA_EDITOR_PLUGINS', PLUGINS))
        self.theme = kwargs.pop('theme', getattr(settings, 'FROALA_EDITOR_THEME', None))
        self.include_jquery = kwargs.pop('include_jquery', getattr(settings, 'FROALA_INCLUDE_JQUERY', True))
        self.image_upload = kwargs.pop('image_upload', True)
        self.file_upload = kwargs.pop('file_upload', True)
        self.language = (getattr(settings, 'FROALA_EDITOR_OPTIONS', {})).get('language', '')
        super(FroalaEditor, self).__init__(*args, **kwargs)

    def get_options(self):

        default_options = {
            'inlineMode': False,
        }

        try:
            image_upload_url = reverse('froala_editor_image_upload')
            default_options['imageUploadURL'] = image_upload_url
            default_options.update([('imageUploadParams', {'csrfmiddlewaretoken': 'csrftokenplaceholder'})])
        except NoReverseMatch:
            default_options['imageUpload'] = False

        try:
            file_upload_url = reverse('froala_editor_file_upload')
            default_options['fileUploadURL'] = file_upload_url
            default_options.update([('fileUploadParams', {'csrfmiddlewaretoken': 'csrftokenplaceholder'})])
        except NoReverseMatch:
            default_options['fileUpload'] = False

        settings_options = getattr(settings, 'FROALA_EDITOR_OPTIONS', {})
        # options = dict(default_options.items() + settings_options.items() + self.options.items())
        options = dict(default_options.items()).copy()
        options.update(settings_options.items())
        options.update(self.options.items())

        if self.theme:
            options['theme'] = self.theme

        json_options = json.dumps(options)
        json_options = json_options.replace('"csrftokenplaceholder"', 'getCookie("csrftoken")')
        return json_options

    def render(self, name, value, attrs=None):
        html = super(FroalaEditor, self).render(name, value, attrs)
        el_id = self.build_attrs(attrs).get('id')
        html += self.trigger_froala(el_id, self.get_options())
        return mark_safe(html)

    def trigger_froala(self, el_id, options):

        str = """
        <script>
            $(function(){
                $('#%s').froalaEditor(%s)
            });
        </script>""" % (el_id, options)
        return str

    def _media(self):
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css',
                    'froala_editor/css/froala_editor.min.css', 'froala_editor/css/froala_style.min.css',
                    'froala_editor/css/froala-django.css')
        }
        js = ('froala_editor/js/froala_editor.min.js', 'froala_editor/js/froala-django.js',)

        if self.include_jquery:
            js = ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.0/jquery.min.js',) + js

        if self.theme:
            css['all'] += ('froala_editor/css/themes/' + self.theme + '.css',)

        if self.language:
            js += ('froala_editor/js/languages/' + self.language + '.js',)

        for plugin in self.plugins:
            js += ('froala_editor/js/plugins/' + plugin + '.min.js',)
            if plugin in PLUGINS_WITH_CSS:
                css['all'] += ('froala_editor/css/plugins/' + plugin + '.min.css',)

        return Media(css=css, js=js)

    media = property(_media)
