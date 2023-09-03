import os
from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

def user_avatar_path(instance, filename):
    return f'user_avatars/{instance.username}/{filename}'

class CustomUser(AbstractUser):
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_users',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_users_permissions',
        related_query_name='custom_user_permission',
    )

    def __str__(self):
        return self.username

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    def __str__(self):
        return self.title



class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('series')
        verbose_name_plural = _('series')
        

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()

    def __str__(self):
        return self.title

class Comic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()


    def __str__(self):
        return self.title