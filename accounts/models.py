from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,phone_number,username,full_name,password):
        if not email:
            raise ValueError("Kindly provide an email.")
        if not phone_number:
            raise ValueError("Kindly provide your phone number.")
        if not username:
            raise ValueError("Kindly provide your username.")
        if not full_name:
            raise ValueError("Kindly provide your full name.")
        user = self.model(email=self.normalize_email(email),phone_number=phone_number,username=username,full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,phone_number,username,full_name,password):
        user = user = self.model(email=self.normalize_email(email),phone_number=phone_number,username=username,full_name=full_name)
        user.set_password(password)
        user.is_admin =True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class CustomUser(AbstractUser):
    username = models.CharField(unique=True,max_length=50,null=False,verbose_name='Username')
    email = models.EmailField(unique=True, max_length=200, null=False, verbose_name='Email Field')
    full_name = models.CharField(unique=False,max_length=150, null=False, verbose_name='Full Name')
    phone_number = PhoneNumberField(region='KE',verbose_name='Phone Number +2547...',null=False,unique=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','full_name','username']
    objects = UserManager()
    
    def __str__(self):
        return self.username