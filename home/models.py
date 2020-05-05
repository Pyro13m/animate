from django.db import models

# Create your models here.
class Review(models.Model):
    Name=models.CharField(max_length=264,null=False)
    Review=models.TextField(null=False)

    def __str__(self):
        return self.Review

