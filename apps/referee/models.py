
import datetime
from datetime import date

from django.db import models
from league.models import League


SEX_CHOICES = (
    ('femenino', 'Femenino'),
    ('masculino', 'Masculino'),
)


class Referee(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    dob = models.DateField()
    stature = models.CharField(max_length=10, blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    nationality = models.CharField(max_length=25, blank=True, null=True)
    sex = models.CharField(
        max_length=15,
        choices=SEX_CHOICES,
        default='Masculino'
    )
    referee_league = models.ForeignKey(
        League, 
        related_name='arbitros',
        blank=True, null=True, 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Arbitro'
        verbose_name_plural = 'Arbitros'
    
    def __str__(self):
        return self.name

    def get_full_name(self):
        return '{} {}'.format(self.name, self.last_name)

    def get_age(self):
        if self.dob:
            today = date.today()
            return today.year-self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        else:
            return None
