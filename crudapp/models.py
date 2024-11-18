from django.db import models

# Create your models here.
class Employee(models.Model):
    empname=models.CharField(max_length=100)
    empemail=models.EmailField()
    empcontact=models.BigIntegerField()
    empcity=models.CharField(max_length=100)
    empsal=models.IntegerField()
    upadated_at=models.DateTimeField(auto_now=True)
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empemail
    
    
class fileupload(models.Model):
    filename=models.CharField(max_length=50)
    file=models.FileField(upload_to='file')