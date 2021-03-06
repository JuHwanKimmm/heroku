from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data published')
    body = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
