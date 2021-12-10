from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.
class User(AbstractBaseUser):
    GENDER_LIST = [
        ("1", "MALE"),
        ("2", "FEMALE"),
        ("3", "OTHERS")
    ]
    username = models.CharField(max_length=6, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=150, blank=False, null=True)
    last_name = models.CharField(max_length=150, blank=False, null=True)
    email = models.EmailField(verbose_name='Email address', null=False, blank=False, unique=True)
    phone = models.CharField(verbose_name='Mobile Number', max_length=10, blank=True, null=True)
    is_staff = models.BooleanField(default=False, db_column='is_staff')
    is_admin = models.BooleanField(default=False, db_column='is_admin')
    is_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=6, blank=True, null=True, choices=GENDER_LIST, default=1)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'password']
    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return '{}-{}'.format(self.email, self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserBiometiceDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aadhar = models.CharField(max_length=16, blank=False, null=False)

    def __str__(self):
        return self.user

    @receiver(post_save, sender=User)
    def update_biometric_details(sender, instance, created, **kwargs):
        if created:
            UserBiometiceDetails.objects.create(user=instance)
            instance.userbiometicedetails.save()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



