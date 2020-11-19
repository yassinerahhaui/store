from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
def image_upload(instance,filename):
    imagename,extension = filename.split('.')
    return "%s/%s.%s"%(instance.category,instance.header,extension)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Store(models.Model):
    header = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    content = RichTextField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    keywords = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.header