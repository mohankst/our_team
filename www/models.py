from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    extentaion = models.CharField(max_length=3)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='staff_images', null=True, blank=True)
    slug = models.SlugField(max_length=40, blank=True)
    responsibilities = models.CharField(max_length=1000, default='')
    bio = models.CharField(max_length=1000, default='')
    facebook = models.CharField(max_length=40, blank=True)
    linkedin = models.CharField(max_length=40, blank=True)
    birthday = models.DateField(default = timezone.now)
    

    def save(self, *args, **kwargs):
    	if not self.pk:
    		self.slug = slugify(self.name)
    	super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
