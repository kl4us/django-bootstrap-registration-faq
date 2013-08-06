from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.paginator import InvalidPage, EmptyPage 
from django.utils import timezone
from django.core.context_processors import csrf
from django.conf import settings
from faq.models import Faq
from django.views.generic import DetailView

def faqs_list(request, slug=None, faq_id=None): 

    template_name='faq/faq_list.html'
    faqs = Faq.objects.filter(draft=False)

    return render_to_response(
        template_name, 
        {
            'faqs': faqs
        }, 
        context_instance=RequestContext(request)
	)       

class FaqDetailView(DetailView):
    methods = ['get']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(
            object=self.object, 
        )
        return self.render_to_response(context)