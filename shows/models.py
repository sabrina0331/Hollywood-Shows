from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=200)
    network = models.CharField(max_length = 50)
    released_date = models.DateField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.title