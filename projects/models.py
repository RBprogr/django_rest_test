from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=255, blank=False)
  description = models.TextField(max_length=255, blank=True, null=True)
  technology = models.CharField(max_length=255, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
