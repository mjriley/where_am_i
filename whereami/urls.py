from django.urls import path

from . import views

urlpatterns = [
    path('update_location', views.update_location, name='update_location'),
    path('process_location', views.process_location, name='process_location'),
    path('', views.display_locations, name='display_locations'),
]
