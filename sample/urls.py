from django.conf.urls.defaults import *
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',

    (r'^$', 'django.views.generic.simple.direct_to_template',
         {'template':'base.html'}, 'index' ),

    (r'^admin/', include(admin.site.urls)),
    (r'', include('django.contrib.auth.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
