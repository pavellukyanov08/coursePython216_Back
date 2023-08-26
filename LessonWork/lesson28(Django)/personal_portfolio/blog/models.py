from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.title
