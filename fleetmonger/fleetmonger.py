import requests
from .vessel import Vessel, vessel_wrapper
from .port import port_wrapper

def _check_params(named):
    if not any(v for v in named.values()):
        raise ValueError("Missing arguments, must provide one of {}".format(named.keys()))

class Fleetmonger(object):

    _version = 'personal-v1'
    _endpoint = 'http://www.fleetmon.com/api/p'

    _status_code = None
    _raw_result = None

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
        self._raw_result, self.status_code = None, None

        params = {k:v for k, v in params.items() if v is not None}
        params['format'] = 'json'
        params['api_key'] = self.api_key
        params['username'] = self.username

        r = requests.get(self._url(resource), params=params)

        self.status_code = r.status_code
        self._raw_result = r.text

        if self.status_code != 200:
            return {}

        return r.json()

    def myfleet(self, **params):
        return vessel_wrapper(self._call('myfleet', **params))

    def vessel(self, imo=None, name=None, lastports=None, **params):
        _check_params({'imo': imo, 'name': name})
        return Vessel(self._call('vessels_terrestrial', imonumber=imo, q=name, lastports=lastports, **params))

    def vesselparticulars(self, imo=None, mmsi=None, name=None, **params):
        _check_params({'imo': imo, 'mmsi': mmsi, 'name': name})
        return Vessel(self._call('vesselparticulars', imonumber=imo, mmsinumber=mmsi, q=name, **params))

    def vesselurl(self, imo=None, mmsi=None, name=None, **params):
        _check_params({'imo': imo, 'mmsi': mmsi, 'name': name})
        return vessel_wrapper(self._call('vesselurl', imonumber=imo, mmsinumber=mmsi, q=name, **params))

    def porturl(self, name=None, locode=None, country=None, **params):
        _check_params({'locode': locode, 'name': name})
        return port_wrapper(self._call('porturl', q=name, locode=locode, country_isocode=country, **params))

    def weather(self, lat=None, lon=None, vessel=None, **params):
        _check_params({'(lat and lon)': lat and lon, 'vessel': vessel})
        if vessel:
            lat, lon = vessel.coords
        return self._call('weather_at_position', lat=lat, lon=lon, **params)

    def containerschedule(self, imo, weeks_ahead=1, **params):
        return port_wrapper(self._call('container_schedule', imo=imo, weeks_ahead=weeks_ahead, **params))
