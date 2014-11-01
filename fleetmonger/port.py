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
        self.arrival = setup_dt(kwargs.get('arrival'))
        self.departure = setup_dt(kwargs.get('departure'))

        self.eta = setup_date(kwargs.get('eta'))
        self.etd = setup_date(kwargs.get('etd'))

        self.locode = kwargs.get('locode') or kwargs.get('port_locode')
        self.name = kwargs.get('name') or kwargs.get('port_name')
    