from django.urls import path

from . import views

urlpatterns = [
	path('', views.country, name="general-index"),
]
