from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='events/')
    is_upcoming = models.BooleanField(default=True)

    def __str__(self):
        return self.title