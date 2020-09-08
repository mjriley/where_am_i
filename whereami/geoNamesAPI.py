import requests


class GeoNamesAPI():
    BASE_URL = 'http://api.geonames.org/search'

    def __init__(self, username):
        self._username = username

    def get_location(self, city):
        response = requests.get(self.BASE_URL, params={
                                'name': city, 'username': self._username, 'maxRows': 10, 'type': 'json'})
        response_json = response.json()
        best_location = response_json['geonames'][0]

        return {
            'name': best_location['name'],
            'country': best_location['countryName'],
            'latitude': best_location['lat'],
            'longitude': best_location['lng'],
        }
