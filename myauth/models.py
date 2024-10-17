from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    """Manager for user"""

    def create_user(self, email, first_name, last_name, password=None):
        """Create a new user"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]


    def get_full_name(self):
        """Retrieve full name of user"""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """Return string representation of our user"""
        return self.email

    class Meta:
        db_table = "user"
