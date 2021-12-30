from django.db import models
from django.core.files import File
from io import BytesIO
from PIL import Image


class Size(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Category(models.Model):
    parent = models.ForeignKey('self',related_name='children',on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    is_featured=models.BooleanField(default=False)
    ordering=models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural='Categories'
        ordering=('ordering',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % (self.slug)
class Product(models.Model):
    
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    parent=models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price=models.FloatField()
    is_featured=models.BooleanField(default=False)
    num_available=models.IntegerField(default=1)
    
    date_added=models.DateTimeField( auto_now_add=True)
    image=models.ImageField(upload_to='uploads/', blank=True,null=True)
    thumbnail=models.ImageField(upload_to='uploads/',blank=True,null=True)
    
    sizes=models.ManyToManyField(Size,blank=True,null=True)
    
    
    class Meta:
        ordering=('-date_added',)
    
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.thumbnail=self.make_thumbnail(self.image)
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug,self.slug)
    
    def make_thumbnail(self,image,size=(800,700)):
        img=Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quantity=85)
        
        thumbnail=File(thumb_io,name=image.name)
        return thumbnail
    
    