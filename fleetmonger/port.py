from datetime import timedelta
from .utils import setup_dt, setup_date


class port_wrapper(list):

    def __init__(self, kwargs):
        super(port_wrapper, self).__init__()

        self.meta = kwargs['meta']
        ports = kwargs['objects']

        for _p in ports:
            self.append(Port(_p))


class Port(object):

    '''A port'''

    def __init__(self, kwargs):
        if kwargs.get('arrival'):
            self.arrival = setup_dt(kwargs['arrival'])
            self.departure = setup_dt(kwargs['departure'])

        if kwargs.get('eta'):
            self.eta = setup_date(kwargs['eta'])
            self.etd = setup_date(kwargs['etd'])

        self.locode = kwargs.get('locode') or kwargs.get('port_locode')
        self.name = kwargs.get('name') or kwargs.get('port_name') or kwargs.get('portname')

    @property
    def duration(self):
        if hasattr(self, 'etd') and hasattr(self, 'eta'):
            return self.etd - self.eta
        elif hasattr(self, 'departure') and hasattr(self, 'arrival'):
            return self.departure - self.arrival

        return None

    def __repr__(self):
        return '<' + self.name + '>'
