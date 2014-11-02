from datetime import datetime
import pytz


def setup_dt(string):
    "2014-10-31 12:10:52+00:00"
    dt = datetime.strptime(string[:-6], '%Y-%m-%d %H:%M:%S')
    return pytz.utc.localize(dt)

def setup_date(string):
    return datetime.strptime(string, '%Y-%m-%d').date()
