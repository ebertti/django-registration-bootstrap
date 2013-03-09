from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template',
         {'template':'base.html'}, 'index' ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django.contrib.auth.urls')),

)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1],
         'django.views.static.serve',
         {'document_root':  settings.MEDIA_ROOT, 'show_indexes': True}),
    )