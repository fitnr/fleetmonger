from .utils import setup_dt
from .port import port_wrapper, Port


class vessel(object):

    """docstring for vessel"""

    # 'name'
    # 'destination'
    # 'etatime'
    # 'flag'
    # 'heading'
    # 'imonumber'
    # 'latitude'
    # 'location'
    # 'longitude'
    # 'mmsinumber'
    # 'navigationstatus'
    # 'photos'
    # 'positionreceived'
    # 'publicurl'
    # 'type'
    # 'last_ports'
    # 'last_port'

    def __init__(self, kwargs):

        if kwargs.get('vessel'):
            kwargs = kwargs['vessel']

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
