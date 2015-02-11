from .utils import setup_dt
from .port import port_wrapper, Port

class vessel_wrapper(list):

    """A list of vessels with a few extra properties"""

    def __init__(self, kwargs):
        super(vessel_wrapper, self).__init__()

        self.meta = kwargs['meta']
        vessels = kwargs['objects']

        for v in vessels:
            self.append(Vessel(v['vessel']))

class Vessel(object):

    """A single vessel"""

    name = None
    destination = None
    etatime = None
    flag = None
    heading = None
    imonumber = None
    latitude = None
    location = None
    longitude = None
    mmsinumber = None
    navigationstatus = None
    photos = None
    positionreceived = None
    publicurl = None
    type = None
    last_ports = None
    last_port = None

    def __init__(self, kwargs):

        if kwargs.get('vessel'):
            kwargs = kwargs['vessel']
        else:
            return

        for k, v in kwargs.items():

            if k in ['positionreceived', 'etatime']:
                setattr(self, k, setup_dt(v))

            elif k == 'last_ports':
                self.last_ports = port_wrapper(v)

            elif k == 'lastport':
                self.last_port = Port(v)

            else:
                setattr(self, k, v)


    @property
    def coords(self):
        return (self.latitude, self.longitude)

    def __repr__(self):
        return '<' + self.name + '>'
