import factory
import factory.fuzzy
import random 
from app import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.conf import settings
import pytz


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Profile
    
    user     = factory.SubFactory('app.factories.UserFactory', profile=None)
    avatar   = factory.django.ImageField(color=factory.Faker('color_rgb'), width=512, height=512)
    location = factory.Faker("city")
    birthday = factory.Faker("date_of_birth")


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('user_name')
    profile = factory.RelatedFactory(ProfileFactory, factory_related_name='user')


class ActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Activity

    name = factory.Faker("sentence", nb_words=10)
    slug = factory.LazyAttribute(lambda x: slugify(x.name))
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")
    body = factory.Faker("paragraph")
    user = factory.fuzzy.FuzzyChoice(User.objects.all())
    likes = factory.fuzzy.FuzzyInteger(0, 9999)
    created_at = factory.fuzzy.FuzzyDateTime(datetime.now(tz=pytz.timezone(settings.TIME_ZONE)) + relativedelta(years=-10))

    @factory.post_generation
    def hubs(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.hubs.add(*extracted)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment
    
    body = factory.Faker("paragraph")
    activity = factory.fuzzy.FuzzyChoice(models.Activity.objects.all())
    user = factory.fuzzy.FuzzyChoice(User.objects.all())
    likes = factory.fuzzy.FuzzyInteger(0, 9999)
    created_at = factory.fuzzy.FuzzyDateTime(datetime.now(tz=pytz.timezone(settings.TIME_ZONE)) + relativedelta(years=-10))


class LinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Link
    
    url = factory.Faker('uri')
    activity = factory.fuzzy.FuzzyChoice(models.Activity.objects.all())
    social = factory.fuzzy.FuzzyChoice(models.Social.objects.all())
    user = factory.fuzzy.FuzzyChoice(User.objects.all())


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Image

    # file = factory.django.FileField(filename='blank_16x9.jpg')
    file = factory.django.ImageField(color=factory.Faker('color_rgb'), width=1600, height=900)
    activity = factory.fuzzy.FuzzyChoice(models.Activity.objects.all())
    user = factory.fuzzy.FuzzyChoice(User.objects.all())


class HubFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Hub
        django_get_or_create = ('name',)

    name = factory.Faker('street_suffix')
    slug = factory.LazyAttribute(lambda x: slugify(x.name))
    user = factory.fuzzy.FuzzyChoice(User.objects.all())
