from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    # Example:
    # (r'^musikbiblio/', include('musikbiblio.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.BASE_DIR+'/core/static/', 'show_indexes': True}),
)
