import requests
from .vessel_wrapper import vessel_wrapper
from .vessel import vessel


class Fleetmonger(object):

    _version = 'personal-v1'
    _endpoint = 'http://www.fleetmon.com/api/p'

    _status_code = None

    """API class for Fleetmon"""

    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    def _url(self, resource):
        return '{endpoint}/{version}/{resource}/'.format(
            endpoint=self._endpoint,
            version=self._version,
            resource=resource
        )

    def _call(self, resource, **params):
        url = self._url(resource)

        params['format'] = 'json'
        params['api_key'] = self.api_key
        params['username'] = self.username

        r = requests.get(url, params=params)

        self.status_code = r.status_code

        return r.json()

    def myfleet(self, **params):
        return vessel_wrapper(self._call('myfleet', **params))

    def vessel(self, imonumber=None, q=None, **params):
        return vessel(self._call('vessels_terrestrial', imonumber=imonumber, q=q, **params))

    def versselurl(self, imo, **params):
        return self._call('versselurl', imo=imo, **params)

    def porturl(self, q, **params):
        return self._call('porturl', q=q, **params)

    def weather_at_position(self, lat, lon, **params):
        return self._call('weather_at_position', lat=lat, lon=lon, **params)

    def container_schedule(self, imo, weeks_ahead=None, **params):
        return self._call('container_schedule', imo=imo, weeks_ahead=weeks_ahead, **params)
