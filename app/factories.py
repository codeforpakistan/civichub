import factory
import factory.fuzzy
from app import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('user_name')

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post
    
    location = factory.Faker("city")

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    name = factory.Faker("sentence", nb_words=10)
    slug = factory.LazyAttribute(lambda x: slugify(x.name))
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")
    hub = factory.fuzzy.FuzzyChoice(models.Hub.objects.all())
    body = factory.Faker("paragraph")
    user = factory.fuzzy.FuzzyChoice(User.objects.all())

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.tags.add(*extracted)

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment
    
    body = factory.Faker("paragraph")
    post = factory.fuzzy.FuzzyChoice(models.Post.objects.all())
    user = factory.fuzzy.FuzzyChoice(User.objects.all())

class LinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Link
    
    url = factory.Faker('uri')
    post = factory.fuzzy.FuzzyChoice(models.Post.objects.all())
    social = factory.fuzzy.FuzzyChoice(models.Social.objects.all())
    user = factory.fuzzy.FuzzyChoice(User.objects.all())

class AttachmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Attachment

    file = factory.django.FileField(filename='blank_16x9.jpg')
    post = factory.fuzzy.FuzzyChoice(models.Post.objects.all())
    user = factory.fuzzy.FuzzyChoice(User.objects.all())

class HubFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Hub

    name = factory.Faker('uri_page')
    slug = factory.LazyAttribute(lambda x: slugify(x.name))
    user = factory.fuzzy.FuzzyChoice(User.objects.all())

class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tag

    name = factory.Faker('uri_page')
    slug = factory.LazyAttribute(lambda x: slugify(x.name))
    user = factory.fuzzy.FuzzyChoice(User.objects.all())