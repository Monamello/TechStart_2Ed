from django.db import models

class Marketplace(models.Model):
    name = models.CharField(max_length=90, verbose_name='nome')
    description = models.CharField(max_length=256, verbose_name='descrição')
    site = models.CharField(max_length=256, verbose_name='site')
    telephone = models.IntegerField(verbose_name='telefone de contato')
    email = models.CharField(max_length=256, verbose_name='e-mail de contato')
    support_contact = models.CharField(max_length=256, verbose_name='contato responsável técnico')
