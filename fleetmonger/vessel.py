from .utils import setup_dt
from .port import Port

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
        self.lastport = Port(kwargs['lastport'])

        