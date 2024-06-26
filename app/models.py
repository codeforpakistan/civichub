from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from dateutil.relativedelta import relativedelta
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Activity(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    hubs = models.ManyToManyField("Hub", blank=True)
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT, related_name='activities')
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "activities"
        verbose_name_plural = "activities"
    
    def __str__(self):
        return self.name
    
    def timesince(self):
        return timesince(self)


class Social(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Link(models.Model):
    url = models.URLField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='links')
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.url


class Image(models.Model):
    file = models.ImageField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='images')
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file.name


class Comment(models.Model):
    body = models.TextField()
    likes = models.IntegerField(default=0)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.get_full_name()} posted in {self.activity.name}'

    def timesince(self):
        return timesince(self)
    
    @property
    def can_edit(self):
        return self.created_at > timezone.now() - datetime.timedelta(minutes=5)


class Hub(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


def timesince(obj):
    d1 = obj.created_at
    d2 = timezone.now()
    delta = relativedelta(d1, d2)

    for comp in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
        attr = getattr(delta, f'{comp}s')
        if attr != 0:
            return f'{abs(attr)} {comp}{"s"[:abs(attr)^1]} ago'
    
    return delta
    