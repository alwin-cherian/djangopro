from django.db import models
class post(models.Model):
    head=models.CharField(max_length=100)
    descr=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    img=models.ImageField(upload_to='picz')



# Create your models here.
