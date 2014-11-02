from .utils import setup_dt
from .port import port_wrapper, Port


class vessel(object):

    """docstring for vessel"""

    def __init__(self, kwargs):

        if kwargs.get('vessel'):
            kwargs = kwargs['vessel']

        self.name = kwargs['name']
        self.destination = kwargs['destination']
        self.etatime = setup_dt(kwargs['etatime'])
        self.flag = kwargs['flag']
        self.heading = kwargs['heading']
        self.imonumber = kwargs['imonumber']

        self.latitude = kwargs['latitude']
        self.location = kwargs['location']
        self.longitude = kwargs['longitude']

        self.mmsinumber = kwargs['mmsinumber']

        self.navigationstatus = kwargs['navigationstatus']
        self.photos = kwargs['photos']
        self.positionreceived = setup_dt(kwargs['positionreceived'])
        self.publicurl = kwargs['publicurl']
        self.type = kwargs['type']

        if kwargs.get('last_ports'):
            self.last_ports = port_wrapper(kwargs['last_ports'])

        if kwargs.get('lastport'):
            self.last_port = Port(kwargs['lastport'])

    @property
    def coords(self):
        return (self.latitude, self.longitude)

    def __repr__(self):
        return '<' + self.name + '>'
