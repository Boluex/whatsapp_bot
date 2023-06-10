from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
def generate_uuid():
    token=str(uuid.uuid4())
    return token
class student_db(models.Model):
    student_name=models.ForeignKey(User,on_delete=models.CASCADE)
    student_info=models.CharField(max_length=3000000,blank=True)
    student_token=models.CharField(max_length=3000000,default=generate_uuid(),unique=True,blank=False)
    
    def save(self,*args,**kwargs):
        self.student_token=generate_uuid()
        super(student_db,self).save(*args,**kwargs)
        
        
class student_notes(models.Model):
    name=models.CharField(max_length=1000,blank=False)
    file=models.FileField(upload_to='pdf_files',blank=False)
    
    
    
    
    
    
    
    
    