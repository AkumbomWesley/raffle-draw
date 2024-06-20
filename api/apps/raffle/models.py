# from django.db import models
#
# from api.apps.core.models import BaseModel
#
#
# class RaffleManager(models.Manager):
#     pass
#
#
# class Raffle(BaseModel, models.Model):
#     name = models.CharField(max_length=40, unique=True)
#
#     objects = RaffleManager()
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Raffle'
#         verbose_name_plural = 'Raffles'
