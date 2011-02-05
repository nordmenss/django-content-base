from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from bname.bname_functions import *
from django.utils.translation import ugettext as _

class IntroField(models.TextField):
    def __init__(self, *args, **kwargs):
        super(IntroField, self).__init__(*args, **kwargs)

class ContentField(models.TextField):
    def __init__(self,*args, **kwargs):
        super(ContentField, self).__init__(*args, **kwargs)

class content_base(models.Model):
    title=models.CharField(max_length=150,null=True,verbose_name=_('Title'))
    #cat = models.ForeignKey(article_category,verbose_name=_('Category'))
    introtext=IntroField(null=False,verbose_name=_('Introtext'))
    published = models.BooleanField(default=True,verbose_name=_('Published'))
    content=ContentField(null=True,verbose_name=_('Content'))
    created=models.DateField(auto_now_add=True,verbose_name=_('Created'))
    modified=models.DateTimeField(auto_now_add=True,null=True,verbose_name=_('Modified'))
    url=models.SlugField(max_length=150,blank=False, null=False,verbose_name=_('url'))
    created_by  = models.ForeignKey(User, related_name="%(class)s_created")
    modified_by = models.ForeignKey(User, null=True,related_name="%(class)s_modified")
    lang=models.CharField(max_length=2,blank=False, null=False,choices=settings.LANGUAGES,verbose_name=_('Lang'))
    #tags = TaggableManager()
    class Meta():
        abstract=True
        #db_table = 'article_model'
        ordering=('-created',)
        verbose_name =  _('Article')
        verbose_name_plural = _('Articles')

class category_base(models.Model):
    title=models.CharField(max_length=150,null=True)
    published = models.BooleanField(default=True)
    content=ContentField(null=True)
    ordering=models.PositiveIntegerField(null=False,default=0)
    metadesc=models.TextField(blank=True,null=True)
    metakeys=models.TextField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    created_by  = models.ForeignKey(User, related_name="%(class)s_created")
    url=models.SlugField(max_length=150,blank=False, null=False)
    lang=models.CharField(max_length=2,blank=False, null=False,choices=settings.LANGUAGES)
    class Meta():
        abstract=True
        #db_table = 'categories'
        ordering=('ordering',)
        verbose_name =  _('Category')
        verbose_name_plural = _('Categories')

    def get_absolute_url(self):
        return settings.FORCE_SCRIPT_NAME+settings.LANGUAGE_CODE+"/c/"+self.url

    def __unicode__(self):
            return self.title