from django.template import RequestContext
from django.shortcuts import render_to_response
from bname.apps.articles.models import *
import django.http as http
import django.shortcuts as shortcuts

def with_tag(request):
    query_tag = Tag.objects.get(name=tag)
    entries = TaggedItem.objects.get_by_model(models.BlogEntry, query_tag)
    entries = entries.filter(lang=settings.LANGUAGE_CODE)
    render_to_response("articles/list.html", c,context_instance=RequestContext(request))

def show_article(request,article_url):
    article=Article.objects.get(url=article_url,lang=settings.LANGUAGE_CODE)
    c = {"article":article}
    return render_to_response("articles/page.html", c,context_instance=RequestContext(request))
