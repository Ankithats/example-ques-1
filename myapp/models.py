from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    
    image=models.ImageField(upload_to='profilephoto')
    desi=models.TextField()
    exp=models.TextField()
    person=models.ForeignKey(User,on_delete=models.CASCADE)
    userr=models.CharField(max_length=200)
    
    def _str_(self):
        return self.userr
