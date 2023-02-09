from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self, firstname, lastname, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, firstname, lastname, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            firstname = firstname,
            lastname = lastname,
        )
        # setting the permissions
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        # saving the user to the database
        user.save(using=self._db)

        return user

class Account(AbstractBaseUser):
    firstname      = models.CharField(max_length=50)
    lastname       = models.CharField(max_length=50)
    username       = models.CharField(max_length=50, unique=True)
    email          = models.EmailField(max_length=100, unique=True)
    phone_number   = models.CharField(max_length=50)

    # Required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    # telling django to use email address as the username
    USERNAME_FIELD = 'email'

    # Required fields
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    # telling account that we are using the MyAccountManager class for these operations
    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    # mandetory methods
    def has_perm(self,perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    