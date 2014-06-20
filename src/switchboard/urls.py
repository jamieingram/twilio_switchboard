from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()
urlpatterns = patterns('')

# Development URL Patterns Only - For example 404 / 500 Page Previews
if settings.DEBUG:
    urls = [
        (r'^404/$', TemplateView.as_view(template_name="404.html")),
        (r'^500/$', TemplateView.as_view(template_name="500.html")),
    ]
    urlpatterns += patterns('', *urls)

# Root Patterns
urls = [
    # Root (To be replaced with creator app
    url(r'', include('switchboard.twiliorouter.urls', namespace="twiliorouter")),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += patterns('', *urls)

''' static + media '''
urlpatterns += patterns('',
                       (r'^s/(.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT}
                        ),
                        ) + static(settings.MEDIA_URL,
                                   document_root=settings.MEDIA_ROOT)
