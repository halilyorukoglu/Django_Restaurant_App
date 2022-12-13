from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# menu/foto-ismi.jpeg
# burger/foto-ismi.jpeg
class LezzET(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="hamburgers")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

   
        
class home(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    integer = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class services(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    integer = models.IntegerField()
    def __str__(self):
        return self.title

    




    

    
    