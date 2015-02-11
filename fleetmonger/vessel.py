from .utils import setup_dt
from .port import port_wrapper, Port


class vessel_wrapper(list):

    """A list of vessels with a few extra properties"""

    def __init__(self, kwargs):
        super(vessel_wrapper, self).__init__()

        self.meta = kwargs['meta']
        vessels = kwargs['objects']

        for v in vessels:
            self.append(Vessel(v))


class Vessel(object):

    """A single vessel"""

    name = 'Vessel'
    destination = None
    etatime = None
    flag = None
    flag_iso = None
    heading = None
    imo = None
    latitude = None
    location = None
    longitude = None
    mmsi = None
    navigationstatus = None
    photos = None
    positionreceived = None
    url = None
    type = None
    last_ports = None
    last_port = None

    def __init__(self, kwargs):

        if kwargs.get('vessel'):
            kwargs = kwargs['vessel']

        for k, v in kwargs.items():
            if not v:
                continue

            if k in ['positionreceived', 'etatime']:
                setattr(self, k, setup_dt(v))

            elif k in ('mmsinumber', 'mmsi'):
                self.mmsi = v

            elif k in ('imonumber', 'imo'):
                self.imo = v

            elif k == 'last_ports':
                self.last_ports = port_wrapper(v)

            elif k == 'lastport':
                self.last_port = Port(v)

            elif k == 'public_url':
                self.url = v

            elif k == 'flag':
                # e.g. "US|United States"
                self.flag_iso, self.flag = v.split('|')

            elif k == 'photos':
                self.photos = v.split('|')

            else:
                setattr(self, k, v)

    @property
    def coords(self):
        return (self.latitude, self.longitude)

    def __repr__(self):
        return '<' + self.name + '>'
