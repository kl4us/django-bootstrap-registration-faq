from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.utils import timezone

from faq.views import FaqDetailView
from faq.models import Faq

urlpatterns = patterns('',
    url(r'^$', 'faq.views.faqs_list', name="faq_list"),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/$', 
        FaqDetailView.as_view(
            queryset=Faq.objects.filter(draft=False),
            context_object_name="faq"
        ),
        name="faq"
    ),    
)