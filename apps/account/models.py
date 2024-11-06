from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.




#model Employee - employee details are stored
class UserData(AbstractBaseUser, PermissionsMixin):  
    email = models.EmailField(unique=True, blank=True, null=True)  
    username = models.CharField(max_length=100, null=True,blank=True) 
    mobile = models.CharField(max_length=15, blank=True, null=True)    
    # Add permission-related fields  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  

    class Meta:
        db_table = 'account_user'

    def __str__(self):
        return self.email if self.email else "Unnamed data"