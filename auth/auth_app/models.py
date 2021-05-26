from django.db import models
from django_mysql.models import ListCharField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create your models here.

class UserProfileManager(BaseUserManager):

    def create_user(self, username, email, age, password = None):
        if not email:
            raise ValueError("User must have a valid email")

        if not age:
            raise ValueError("User must enter age")

        email = self.normalize_email(email)
        user = self.model(username = username, email=email, age=age)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, age, password):
        user = self.create_user(username, email, age, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Model for users in the system"""
    # phone_no = PhoneNumberField(unique = True)
    username = models.CharField(max_length = 100, unique=True, blank=False)
    email = models.EmailField(max_length = 255)
    age = models.IntegerField()
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "age"]

    def get_full_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_age(self):
    	return self.age

    # def get_phone_no(self):
        # return self.phone_no

    def __str__(self):
        return str(self.username) + " " + str(self.email) + " " + str(self.age)


class Shows(models.Model):
    """ Model for a shop"""
    title = models.CharField(max_length = 500)
    genre = ListCharField(
    	base_field = models.CharField(max_length = 100),
    	size = 3,
    	max_length = (3*101)
    )
    platform = models.CharField(max_length = 100)
    rating = models.DecimalField(max_digits = 3, decimal_places = 1)
    episode = models.IntegerField()
    def __str__(self):
        return "title : " + str(self.title) + " platform : " + str(self.platform) + " rating : " + str(self.rating)+ " episode : " + str(self.episode)
