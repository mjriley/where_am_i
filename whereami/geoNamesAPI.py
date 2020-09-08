import requests


NAMES_LIST_KEY = 'geonames'


class GeoNamesAPI():
    BASE_URL = 'http://api.geonames.org/search'

    def __init__(self, username):
        self._username = username

    def get_location(self, city):
        response = requests.get(self.BASE_URL, params={
                                'name': city, 'username': self._username, 'maxRows': 10, 'type': 'json'})
        response_json = response.json()

        if len(response_json[NAMES_LIST_KEY]) == 0:
            # no valid results found
            return None

        best_location = response_json[NAMES_LIST_KEY][0]

        return {
            'name': best_location['name'],
            'country': best_location['countryName'],
            'latitude': best_location['lat'],
            'longitude': best_location['lng'],
        }
