from datetime import datetime

def setup_dt(string):
    "2014-10-31 12:10:52+00:00"
    return datetime.strptime(string[:-6], '%Y-%m-%d %H:%M:%S')

def setup_date(string):
    return datetime.strptime(string, '%Y-%m-%d').date()
