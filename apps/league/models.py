#django core
from django.db import models
#reusable apps
from reusable.constants import *



class League(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='logo-league/')
    email = models.EmailField(default='contact@micorreo.com')

    class Meta:
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligas'
    
    def __str__(self):
        return 'Liga: {}'.format(self.name)


class Directive(models.Model):
    league_directive = models.OneToOneField(
        League, 
        related_name='league_directive',
        on_delete=models.CASCADE
    )
    president = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Directiva'
    
    def __str__(self):
        return 'Directiva de {}'.format(self.league_directive.name)

        
class Rules(models.Model):
    league_rules = models.ForeignKey(
        League, 
        blank=True, null=True, 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, **NULL)
    file = models.FileField(upload_to='rules_file')

    class Meta:
        verbose_name = 'Reglamento'
        verbose_name_plural = 'Reglamentos'

    def __str__(self):
        return 'Reglamento de {}'.format(self.league_rules.name)


class Stadium(models.Model):
    league_stadium = models.ForeignKey(
        League, 
        **NULL, 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=120, **NULL)
    adress = models.CharField(max_length=120, **NULL)
    longitud = models.FloatField(**NULL, default=None)
    latitude = models.FloatField(**NULL, default=None)

    class Meta:
        verbose_name = 'Campo'
        verbose_name_plural = 'Campos'
    
    def __str__(self):
        return 'Campo {} de {}'.format(self.name, self.league_stadium)
    