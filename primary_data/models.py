from django.db import models
from django.utils.text import slugify
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=200)
    iso2 = models.CharField(max_length=50, blank=True)
    iso3 = models.CharField(max_length=50, blank=True)
    phone_code = models.CharField(blank=True, max_length=100)
    capital = models.CharField(max_length=100, blank=True)
    currency = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Citie(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    state = ChainedForeignKey(
                            State,
                            chained_field="country",
                            chained_model_field="country",
                            null=True,
                            blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    book_slug = models.SlugField(max_length=150, unique=True)
    primary_author_first_name = models.CharField(
                                                "Author First",
                                                max_length=100,
                                                blank=True)
    primary_author_last_name = models.CharField(
                                                "Author Last",
                                                max_length=100,
                                                blank=True)
    pub_date = models.DateField("Book Pub Date", blank=True, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=150)
    subject_slug = models.SlugField(max_length=150, unique=True)
    code = models.CharField(max_length=250)
    book = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name + " " + self.code


class Universitie(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    domain = models.CharField(max_length=200, blank=True)
    web_page = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
