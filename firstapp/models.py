from django.db import models
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField() 
    def __str__(self):
        return self.name
#cuisine model
STATUS_CHOICES = (
   ('draft', 'Draft'),
   ('published', 'Published'),
)
CATG_CHOICES = (
    ('dessert', 'Dessert'),
   ('snack', 'Snack'),
   ('food', 'Food'),
)

class Cuisine(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=15,      choices = (('veg','Veg'),('non veg','NON Veg')),    default = 'non veg')
    catg = models.CharField(max_length=8,  choices=CATG_CHOICES,default = 'food')
    desc =models.TextField()
    author = models.ForeignKey(User,         related_name='cuisine_user',     on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=30, unique_for_date='publish')
    status = models.CharField(max_length=10,
                             choices=STATUS_CHOICES,
                             default='draft')
    
    def __str__(self):
       return self.name
