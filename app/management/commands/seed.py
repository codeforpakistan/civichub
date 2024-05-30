from app import models, factories
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

from random import randrange


class Command(BaseCommand):

    help = "Generates initial data for testing"

    def handle(self, *args, **options):
        self.create_admin()
        self.create_users(10)
        self.create_socials()
        self.create_hubs(20)
        self.create_activities(50)
        self.create_links(100)
        self.create_comments(200)
        self.create_images(200)

    def create_admin(self):
        try:
            user = User.objects.create_superuser(
                username="admin",
                email="info@example.com",
                password="admin",
                first_name="System",
                last_name="Administrator",
            )
            self.stdout.write(self.style.SUCCESS('Admin created: "%s"' % user))
        except:
            pass
    
    def create_users(self, num=1):
        for _ in range(num):
            item = factories.UserFactory()
            self.stdout.write(self.style.SUCCESS('User created: "%s"' % item))
    
    def create_socials(self):
        platforms = ['Facebook','Instagram','Twitter','LinkedIn','TikTok','YouTube','GitHub']
        for p in platforms:
            item = models.Social.objects.create(name=p)
            self.stdout.write(self.style.SUCCESS('Social created: "%s"' % item))

    def create_activities(self, num=1):
        for _ in range(num):
            item = factories.ActivityFactory.create(
                hubs=models.Hub.objects.all().order_by("?")[:3],
            )
            self.stdout.write(self.style.SUCCESS('Activity created: "%s"' % item))
    
    def create_comments(self, num=1):
        for _ in range(num):
            item = factories.CommentFactory()
            self.stdout.write(self.style.SUCCESS('Comment created: "%s"' % item))
        
    def create_links(self, num=1):
        for _ in range(num):
            item = factories.LinkFactory()
            self.stdout.write(self.style.SUCCESS('Link created: "%s"' % item))
    
    def create_images(self, num=1):
        for _ in range(num):
            item = factories.ImageFactory()
            self.stdout.write(self.style.SUCCESS('Image attached: "%s"' % item))

    def create_hubs(self, num=1):
        for _ in range(num):
            item = factories.HubFactory()
            self.stdout.write(self.style.SUCCESS('Hub created: "%s"' % item))
    