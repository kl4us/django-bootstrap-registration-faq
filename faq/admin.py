from django.contrib import admin
from faq.models import Faq
from django_summernote.admin import SummernoteModelAdmin

class FaqAdmin(SummernoteModelAdmin):
    list_display = ('question', 'answer', 'sort_order', 'draft')
    list_filter = ['draft']
    search_fields = ['question', 'answer']
    list_editable = ['sort_order', 'draft']
    prepopulated_fields = {"slug":("question",)}

admin.site.register(Faq, FaqAdmin)  