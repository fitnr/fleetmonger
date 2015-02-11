from .utils import setup_dt


class weather(object):

    def __init__(self, kwargs):
        self.arg = kwargs['arg']

        self.temperature_air = kwargs['temperature_air']
        self.pressure = kwargs['pressure']
        self.ice_cover = kwargs['ice_cover']
        self.wind_dir = kwargs['wind_dir']
        self.wind_speed = kwargs['wind_speed']
        self.wind_gust = kwargs['wind_gust']
        self.wave_sigh = kwargs['wave_sigh']
        self.wave_dir = kwargs['wave_dir']
        self.wave_per = kwargs['wave_per']
        self.timestamp = setup_dt(kwargs['timestamp'])
