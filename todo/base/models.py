from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    # anytime the save method is called a timestamp is taking
    update = models.DateTimeField(auto_now=True) 
    # created only takes a timestamp when we first save or create an instance
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update','-created']

    def __str__(self):
        return self.title
