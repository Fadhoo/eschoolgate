from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.user_type = 5
        user.is_staff = True
        user.is_superuser = True

        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
        (3, 'secretary'),
        (4, 'supervisor'),
        (5, 'admin'),
    )

    objects = UserManager()
    username = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(unique=True, max_length=225)
    USERNAME_FIELD = 'email'
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    ordering = ('created',)

    def get_full_name(self):
        return self.email

    def __unicode__(self):
        return self.email


class CommonInfo(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    profile_picture = models.ImageField(blank=True, upload_to='profile_pic')
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)
    school = models.TextField(max_length=500, blank=True)
    state = models.CharField(max_length=30, blank=True)
    local_government = models.CharField(max_length=30, blank=True)

    class Meta:
        abstract = True


class Profile(CommonInfo):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    present_class = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
