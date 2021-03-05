from django.db import models

class SalesPerson(models.Model):
    name = models.CharField(max_length=30, verbose_name='nome fantasia')
    company_name = models.CharField(max_length=90, verbose_name='razão social')
    cnpj = models.IntegerField(verbose_name='cnpj')
    email = models.CharField(max_length=256, verbose_name='e-mail de contato')
    telephone = models.IntegerField(verbose_name='telefone de contato')
    address = models.ForeignKey('Address', on_delete=models.CASCADE, verbose_name='endereço')
    created_at = models.DateField(auto_now_add=True, verbose_name='data de criação')
    update_at = models.DateField(auto_now=True, verbose_name='data de atualização')


    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=256, verbose_name='rua')
    number = models.IntegerField(verbose_name='número')
    neighborhood = models.CharField(max_length=90, verbose_name='bairro')
    complement_address = models.CharField(max_length=256, verbose_name='complemento')

    def __str__(self):
        return self.street
