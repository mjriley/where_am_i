from ..models import User
from ..geoNamesAPI import GeoNamesAPI


class LocationService:
    @staticmethod
    def update_location(email, city_name, time=None):
        # First validate the user -- if the user doesn't exist, there is no point in sending the API request
        user = User.objects.filter(email=email).first()

        if user is None:
            raise Exception(f'Invalid email: {email}')

        # TODO -- fetch username/password from the environment
        api = GeoNamesAPI(username='dimagi')
        retrieved_location = api.get_location(city)
        if retrieved_location is None:
            raise Exception(f'No location found for: {city_name}')

        return user.update_location(retrieved_location, time=time)
