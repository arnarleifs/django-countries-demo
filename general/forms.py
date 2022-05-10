from django.forms import ModelForm
from django_countries.widgets import CountrySelectWidget
from general import models


class CountryForm(ModelForm):
	class Meta:
		model = models.Country
		fields = ('country',)
		widgets = {'country': CountrySelectWidget()}
