from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_sms.views.home', name='home'),
    # url(r'^django_sms/', include('django_sms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^faq/', include('faq.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
)
