from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    #codigo = models.IntegerField(null=True,blank=True)
    


    def __str__(self):
        return self.username
    
    def nombre_completo(self):
        return self.first_name +" "+ self.last_name