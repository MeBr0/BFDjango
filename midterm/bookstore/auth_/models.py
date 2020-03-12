from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models


# Copy of AbstractUser + field is_super_admin
class MyAbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField('username',
                                max_length=30,
                                unique=True,
                                validators=[username_validator],
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                },
                                )
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    email = models.EmailField('email address', blank=True)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=
        'Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.'
        ,
    )

    is_super_admin = models.BooleanField(null=True, default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        abstract = True

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_guest(self):
        return not self.is_super_admin


# Copy of User
class MyUser(MyAbstractUser):
    pass


# User profile with one-to-one relation
class UserProfile(models.Model):
    id = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=10)
    rnn = models.CharField(max_length=12)
