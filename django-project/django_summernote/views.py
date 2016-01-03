from django.http import (
    HttpResponseBadRequest,
    HttpResponseServerError,
    HttpResponseForbidden,
)
from django.shortcuts import render
from django_summernote.models import Attachment
from django_summernote.settings import summernote_config


def editor(request, id):
    return render(
        request,
        'django_summernote/widget_iframe_editor.html',
        dict({
            'id_src': id,
            'id': id.replace('-', '_'),
        })
    )


def upload_attachment(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Only POST method is allowed')

    if summernote_config['attachment_require_authentication']:
        if not request.user.is_authenticated():
            return HttpResponseForbidden('Only authenticated users are allowed')

    if not request.FILES.getlist('files'):
        return HttpResponseBadRequest('No files were requested')

    try:
        attachments = []

        for file in request.FILES.getlist('files'):
            attachment = Attachment()
            attachment.file = file
            attachment.name = file.name

            if file.size > summernote_config['attachment_filesize_limit']:
                return HttpResponseBadRequest(
                    'File size exceeds the limit allowed and cannot be saved'
                )

            attachment.save()
            attachments.append(attachment)

        return render(request, 'django_summernote/upload_attachment.json', {
            'attachments': attachments,
        })
    except IOError:
        return HttpResponseServerError('Failed to save attachment')
