from django.db import models


class Photo(models.Model):

    LICENSES = (
        ('RIG', 'Copyright'),
        ('LEF', 'Copyleft'),
        ('CC', 'Creative commons')
    )

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField()
    license = models.CharField(max_length=3, choices=LICENSES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
