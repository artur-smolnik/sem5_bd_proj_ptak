# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Klienci(models.Model):
    idklienta = models.AutoField(primary_key=True)
    imie = models.TextField(blank=True, null=True)
    nazwisko = models.TextField(blank=True, null=True)
    telefonkontaktowy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'klienci'


class Magazyn(models.Model):
    idsprzetu = models.AutoField(primary_key=True)
    typ = models.CharField(max_length=30, blank=True, null=True)
    rozmiar = models.SmallIntegerField(blank=True, null=True)
    kolor = models.CharField(max_length=20, blank=True, null=True)
    czyuszkodzony = models.BooleanField(blank=True, null=True)
    czywypozyczony = models.BooleanField(blank=True, null=True)
    cena = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magazyn'


class Pracownicy(models.Model):
    idpracownika = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30, blank=True, null=True)
    nazwisko = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pracownicy'


class Wypozyczenia(models.Model):
    idwypozyczenia = models.AutoField(primary_key=True)
    idpracownika = models.ForeignKey(Pracownicy, models.DO_NOTHING, db_column='idpracownika')
    idsprzetu = models.ForeignKey(Magazyn, models.DO_NOTHING, db_column='idsprzetu')
    idklienta = models.ForeignKey(Klienci, models.DO_NOTHING, db_column='idklienta')
    datawypozyczenia = models.DateField(blank=True, null=True)
    datazakonczeniawypozyczenia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wypozyczenia'
