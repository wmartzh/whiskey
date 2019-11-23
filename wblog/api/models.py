from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    
    def create_user(self,email,username,first_name="",last_name="",password=None,active=True,is_staff=False,is_admin=False,is_active=True,is_superuser=False):
        if not email:
            raise ValueError("User must have an email address")
        
        if not password:
            raise ValueError("Usrs must have a password")
        
        user_obj = self.model(
            email= self.normalize_email(email)
        )
        user_obj.username = username
        user_obj.first_name = first_name
        user_obj.last_name = last_name 
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_superuser = is_superuser
        user_obj.active = is_active
        user_obj.save(using=self._db)

        return user_obj
        

    def create_staffuser(self, email,username, password):
        user = self.create_user(email, username, password=password, is_staff=True, is_admin=True)
        
        return user

    def create_admin(self, username,first_name,last_name,email,password):
        user = self.create_user(email=email,username=username,first_name=first_name,last_name=last_name,password=password, is_staff=True,is_active=True,is_admin=True,is_superuser=False)
        return  user

    def create_superuser(self,email,username,password,):
        user = self.create_user(email,username, password=password, is_staff=True,is_admin=True, is_superuser=True)
        return user


class User(AbstractUser):
    
    objects = UserManager() 

    email       = models.EmailField(max_length=255, unique=True)
    first_name  = models.CharField(max_length=12)
    last_name   = models.CharField(max_length=12)
    username    = models.CharField(max_length=15, unique=True)
    active      = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email','password']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name():
        return self.username
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
    

class Post(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    title   = models.TextField(max_length=120, null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user)

    @property
    def owner(self):
        return self.user