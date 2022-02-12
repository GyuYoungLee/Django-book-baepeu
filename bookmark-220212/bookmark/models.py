from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        return reverse('bookmark:detail', kwargs={'pk': self.id})
