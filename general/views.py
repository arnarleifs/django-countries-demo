from django.shortcuts import render
from general.forms import CountryForm


def country(request):
	return render(request, 'general/index.html', {
		'form': CountryForm()
	})
