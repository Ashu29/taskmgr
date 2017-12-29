# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.contrib.auth.base_user import BaseUserManager

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.

class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields['is_staff'] = False
        extra_fields['is_superuser'] = False
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model having email as primary field instead of username
    """

    FIELDS_CHARACTER_LIMIT = {
        'FIRST_NAME': 35,
        'LAST_NAME': 35,
        'EMAIL_LIMIT': 255
    }

    first_name = models.CharField('first name', max_length=FIELDS_CHARACTER_LIMIT['FIRST_NAME'], blank=True, null=True)
    last_name = models.CharField('last name', max_length=FIELDS_CHARACTER_LIMIT['LAST_NAME'], blank=True, null=True)
    email = models.EmailField(max_length=FIELDS_CHARACTER_LIMIT['EMAIL_LIMIT'], unique=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=datetime.now)
    is_staff = models.BooleanField('staff status',
                                   default=False,
                                   help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active',
                                    default=True,
                                    help_text='Designates whether this user should be treated as active.'
                                              ' Unselect this instead of deleting accounts.')

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = MyUserManager()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def save(self, *args, **kwargs):
        # Always save the email in lowercase
        self.email = self.email.lower()
        super(MyUser, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{}:{}'.format(self.get_full_name(), self.email)
