from django import forms
from django.contrib import admin
from ckeditor.fields import RichTextField
from ckeditor_widget.widgets import *
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class content_base_admin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (('title','url','lang'),'published')}),
        #(_("Intro, tags"), {'fields':('introtext','tags')}),
        (_("Intro"), {'fields':('introtext',)}),
        (_("Content"), {'fields': ('content',)}),
        (_('Created'), {'fields': (('created','created_by',),)}),
        (_('Modified'), {'fields': (('modified','modified_by',),)}),
    )
    formfield_overrides = {
       IntroField:{"widget":CKEditorWidget(config_name='introtext')},
       ContentField:{"widget":CKEditorWidget(config_name='content')},
       #TaggableManager:{"widget":forms.TextInput(attrs={'size':'100'})},
       RichTextField:{"widget":CKEditorWidget(config_name='content')},
    }
    #list_display=('title','lang_flag','published','url_html','created','introtext_html','tags_str',)
    list_display=('title_str','lang_flag','published','created','introtext_html',)
    date_hierarchy = 'created'
    search_fields=('title','url',)
    list_filter = ('lang','published',)
    #list_editable=('published',)
    readonly_fields=('created','modified','created_by','modified_by',)
    prepopulated_fields = {"url": ("title",)}

    class Media:
        js_base_url = getattr(settings, 'TAGGING_AUTOCOMPLETE_JS_BASE_URL','%sjquery-autocomplete' % settings.MEDIA_URL)
        css = {
            'all': ('%s/jquery.autocomplete.css' % js_base_url,settings.MEDIA_URL+'css/admin/tags.css'),
        }
        js = (
            '%s/lib/jquery.js' % js_base_url,
            '%s/jquery.autocomplete.js' % js_base_url,
            )

    def tags_str(self, obj):
        result=""
        for tag in obj.tags.all():
            if result!="":
                result+=", "
            result+="<b>"+unicode(tag.name)+"</b>"
        return result
    tags_str.short_description = 'Tags'
    tags_str.allow_tags=True

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

    def lang_flag(self, obj):
        return "<nobr>"+get_lang_title(obj.lang)+' <img src="'+settings.MEDIA_URL+'img/flags/'+obj.lang+'.gif" /></nobr>'
    lang_flag.short_description = 'lang'
    lang_flag.allow_tags=True


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
        (None, {'fields': (('title','url','lang'),('published','ordering'))}),
        (_("Content"), {'fields': ('content',)}),
        (_('Created'), {'fields': (('created','created_by',),)}),
        (_('Meta'), {'fields': (('metadesc','metakeys',),)}),
    )
    formfield_overrides = {
       ContentField:{"widget":CKEditorWidget(config_name='content')},
    }
    list_display=('title','lang','published','url','created','ordering',)
    list_editable=('published','ordering',)
    list_filter = ('title', )
    readonly_fields=('created','created_by',)
    prepopulated_fields = {"url": ("title",)}

    def lang_flag(self, obj):
        return get_lang_title(obj.lang)+' <img src="'+settings.MEDIA_URL+'img/flags/'+obj.lang+'.gif" />'
    lang_flag.short_description = 'lang'
    lang_flag.allow_tags=True

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance

#admin.site.register(content, content_admin)
#admin.site.register(category, category_admin)
