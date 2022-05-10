from django.db import models
from django_countries.fields import CountryField


class Country(models.Model):
	country = CountryField()
