from django.db import models
from django.utils.text import slugify


class Services(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    duration = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name