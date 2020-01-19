from django.contrib import admin
from .models import *


# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'iso2', 'iso3',
                    'phone_code', 'capital', 'currency', )
    list_display_links = ('name', )
    search_fields = (
                    'name', 'iso2', 'iso3',
                    'phone_code', 'capital', 'currency', )
    list_filter = ('currency', )
    list_per_page = 50


class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', )
    list_display_links = ('name', )
    search_fields = ('name', 'country', )
    list_filter = ('country', )
    list_per_page = 100


class CitieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state', 'country', )
    list_display_links = ('name', )
    search_fields = ('name', )
    list_filter = ('country', )
    list_per_page = 100


class UniversitieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'domain', 'web_page', 'country', )
    list_display_links = ('name', )
    search_fields = ('name', 'domain', 'web_page', )
    list_filter = ('country', )
    list_per_page = 100


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', )
    list_display_links = ('name', )
    search_fields = ('name', 'code', )
    list_per_page = 100
    prepopulated_fields = {"subject_slug": ("name", )}


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'primary_author_first_name',
                    'primary_author_last_name', 'pub_date')
    list_display_links = ('name', )
    search_fields = ('name', )
    list_per_page = 100
    fields = (
                'name', 'book_slug',  'primary_author_first_name',
                'primary_author_last_name', 'pub_date')
    prepopulated_fields = {"book_slug": ("name", )}


admin.site.register(Country,  CountryAdmin)
admin.site.register(State,  StateAdmin)
admin.site.register(Citie,  CitieAdmin)
admin.site.register(Universitie,  UniversitieAdmin)
admin.site.register(Subject,  SubjectAdmin)
admin.site.register(Book,  BookAdmin)
