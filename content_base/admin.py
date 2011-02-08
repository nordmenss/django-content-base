from django import forms
from django.contrib import admin
from content_base.models import *
from ckeditor.fields import RichTextField
from ckeditor_widget.widgets import *
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class content_base_admin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (('title','url'),'published')}),#(_("Intro, tags"), {'fields':('introtext','tags')}),
        #(_("Category"), {'fields':('cat',)}),
        (_("Intro"), {'fields':('introtext',)}),#(_("Intro, tags"), {'fields':('introtext','tags')}),
        (_("Content"), {'fields': ('content',)}),
        (_('Created'), {'fields': (('created','created_by',),)}),
        (_('Modified'), {'fields': (('modified','modified_by',),)}),
    )
    formfield_overrides = {
       IntroField:{"widget":CKEditorWidget(config_name='introtext')},
       ContentField:{"widget":CKEditorWidget(config_name='content')},
       RichTextField:{"widget":CKEditorWidget(config_name='content')},
    }
    #list_display=('title','lang_flag','published','url_html','created','introtext_html','tags_str',)
    list_display=('title_str','published','created','introtext_html',)
    date_hierarchy = 'created'
    search_fields=('title','url',)
    list_filter = ('published',)#list_filter = ('lang','published',)
    list_editable=('published',)
    readonly_fields=('created','modified','created_by','modified_by',)
    prepopulated_fields = {"url": ("title",)}

    def introtext_html(self, obj):
        return "%s" % (obj.introtext)
    introtext_html.short_description = _('Introtext')
    introtext_html.allow_tags=True

    def title_str(self, obj):
        return "%s" % ("<nobr>"+obj.title+"</nobr>")
    title_str.short_description = _('Title')
    title_str.allow_tags=True

    def url_html(self, obj):
        return "%s" % (obj.url+".html")

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.modified_by = request.user
        instance.save()
        form.save_m2m()
        return instance

class category_base_admin(admin.ModelAdmin):
    fieldsets = (
        #(None, {'fields': (('title','url','lang'),('published','ordering'))}),
        (None, {'fields': (('title','url'),('published','ordering'))}),
        (_("Content"), {'fields': ('content',)}),
        (_('Created'), {'fields': (('created','created_by',),)}),
        (_('Meta'), {'fields': (('metadesc','metakeys',),)}),
    )
    formfield_overrides = {
       ContentField:{"widget":CKEditorWidget(config_name='content')},
    }
    list_display=('title','published','url','created','ordering',)
    list_editable=('published','ordering',)
    list_filter = ('title', )
    readonly_fields=('created','created_by',)
    prepopulated_fields = {"url": ("title",)}

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance

#admin.site.register(content, content_admin)
#admin.site.register(category, category_admin)
