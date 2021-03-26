from django.db import models

# Create your models here.

class Destination() :
    name = models.CharField(max_length=100)
    title : str
    add : str
    contact_no : int 
    mail_id : str
    name : str
    dis : str
class Abc:
    name : str 
    discription : str
    img : str
class Data_base(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    dis = models.TextField() 