from .geoNamesAPI import GeoNamesAPI

from django.shortcuts import render
from whereami.models import User, Location


# Create your views here.

def display_locations(request):
    users = User.objects.all()

    # Should be replaced with however django does JOIN statements, but I can't figure it out
    for user in users:
        # current_location = Location.objects.filter(user=user, current=True)
        user.location = user.get_current_location()

    return render(request, 'whereami/locations.html', context={'users': users})


def update_location(request):
    return render(request, 'whereami/location_form.html')


def process_location(request):
    email = request.POST['email']
    city = request.POST['city']

    # First validate the user -- if the user doesn't exist, there is no point in sending the API request
    user = None
    users = User.objects.filter(email=email)
    if users.count() == 0:
        # Invalid user, return
        return render(request, 'whereami/location_form.html', {'error': f'invalid email specified: {email}'})
    else:
        user = users[0]

    # Otherwise, initiate the API request
    # TODO -- fetch username/password from the environment
    api = GeoNamesAPI(username='dimagi')
    retrieved_location = api.get_location(city)

    location = user.update_location(retrieved_location)

    return render(request, 'whereami/location_submitted.html', {'location': location})
