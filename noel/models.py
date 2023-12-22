from django.db import models

from django.utils import timezone

class SubCategory(models.Model):
   
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to='mycakes/images', default='mycakes/images/default.png')

    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='mycakes/images', default='mycakes/images/default.png')   
    public_day = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.name
    
class Text(models.Model):
    name = models.CharField(max_length=250)


from django.db import models

class Achievement(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
