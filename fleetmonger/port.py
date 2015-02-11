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
    country_isocode = None
    country_name = None
    name = None
    locode = None

    def __init__(self, kwargs):
        if kwargs.get('arrival'):
            self.arrival = setup_dt(kwargs['arrival'])
            self.departure = setup_dt(kwargs['departure'])

        if kwargs.get('eta'):
            self.eta = setup_date(kwargs['eta'])
            self.etd = setup_date(kwargs['etd'])

        for k, v in kwargs.items():
            if k in ('eta', 'etd', 'arrival', 'departure'):
                pass

            elif k in ('name', 'port_name', 'portname'):
                setattr(self, 'name', v)

            elif k in ('locode', 'port_locode'):
                setattr(self, 'locode', v)

            elif k == 'publicurl':
                setattr(self, 'url', v)

            else:
                setattr(self, k, v)

    @property
    def duration(self):
        if hasattr(self, 'etd') and hasattr(self, 'eta'):
            return self.etd - self.eta
        elif hasattr(self, 'departure') and hasattr(self, 'arrival'):
            return self.departure - self.arrival

        return None

    def __repr__(self):
        return '<' + self.name + '>'
