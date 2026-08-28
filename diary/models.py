from django.db import models


# Create your models here.
class DiaryEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
