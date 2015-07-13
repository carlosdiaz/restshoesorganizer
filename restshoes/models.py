from django.db import models

class RestShoes(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    model = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
