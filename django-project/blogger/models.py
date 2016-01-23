from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from .managers import PostManager
from blanc_basic_assets.models import Image


class ClassName(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


BLOG_SETTINGS = settings.BLOG_SETTINGS['defaults']


class Person(models.Model):
    first_name = models.CharField(max_length=30)

    # class Meta:
    #     proxy = True

    def get_absolute_url(self):
        return super(Person, self).get_absolute_url()

    def __unicode__(self):
        return super(Person, self).__unicode__()


class Author(User):
    """A Proxy for User. Overrides some getters"""

    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('author_archive',
                       args=['-'.join([self.first_name, self.last_name])])

    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])


class Postable(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        abstract = True

class Recipe(Postable):
    

class Post(models.Model):
    """
    User generated blog post
    """
    app_label = "blogger"
    model_name = "post"

    header = models.ForeignKey(Image, blank=True, null=True)

    author = models.ForeignKey(User, blank=True, verbose_name=_("author"))
    title = models.CharField(max_length=200, unique=True,
                             verbose_name=_("title"))
    body = models.TextField(verbose_name=_("body"))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_("created at"))
    publish_at = models.DateTimeField(verbose_name=_("publish at"))
    # TODO: last modified?
    published = models.BooleanField(default=BLOG_SETTINGS['auto_publish'],
                                    verbose_name=_("published?"))
    promoted = models.BooleanField(default=BLOG_SETTINGS['auto_promote'],
                                   verbose_name=_("promoted?"))
    # models.ManyToManyField(Tag, blank=True, verbose_name=_("tags"))
    tags = TaggableManager()
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name=_("slug"))

    objects = models.Manager()  # The default manager.
    popular_posts = PostManager()

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_post', args=[str(self.slug)])

    def get_tags(self):
        """Returns tags as a composite string"""
        names = ', '.join([t.name for t in self.tags.all()])
        # if len(names) > 20:
        #    names = names[:20] + "..."
        return names
    get_tags.short_description = _("Tags")
