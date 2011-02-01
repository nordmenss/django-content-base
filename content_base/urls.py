from django.conf.urls.defaults import *
from bname.apps.articles.views import *

urlpatterns = patterns('',
    #(r'^$', show_articles),
    (r'^(.*)\.html$', show_article),
)