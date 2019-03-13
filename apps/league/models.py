from django.db import models


class League(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='logo-league/')


class Directive(models.Model):
    league = models.OneToOneField(League, related_name='league_directive')
    president = models.CharField(max_length=100)
    