from django.db import models


class Doc(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    standardized_content = models.TextField()
    created_at = models.DateTimeField("created_at")

    def __str__(self):
        return self.name
