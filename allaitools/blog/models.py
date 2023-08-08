from django.db import models
from django.urls import reverse


# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to ="media/images")
    
    
    class Meta:
        verbose_name_plural = 'blogs'
        
    def get_absolute_url(self):
        return reverse('blog:product_detail', args=[self.slug])
        
    def __str__(self):
        return self.title
