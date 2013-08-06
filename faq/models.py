from django.db import models

class Faq(models.Model):
    question = models.CharField(max_length=100, null=False)  
    slug = models.SlugField()      
    answer = models.TextField(null=False)
    draft = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.question

    def get_absolute_url(self):
        return '/' + self.slug + '/'    

    class Meta:
         ordering = ["sort_order"]      