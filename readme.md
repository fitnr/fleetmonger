## Fleetmonger

Python wrapper for the [fleetmon.com](fleetmon.com) ship-tracking API.

## API Calls
[Read the details of the API at Fleetmonger](https://www.fleetmon.com/faq/public_api).
* fleetmonger.myfleet
* fleetmonger.vessel
* fleetmonger.vesselparticulars
* fleetmonger.vesselurl
* fleetmonger.porturl
* fleetmonger.weather
* fleetmonger.containerschedule

Note that some API calls require the purchase of credits at Fleetmon. This package is unaffiliated with Fleetmon, use at your own risk.

# Usage

````python
from fleetmonger import Fleetmonger

fm = Fleetmonger('username', 'your key')

fleet = fm.myfleet()

for ship in fleet:
    print ship.name, ship.destination
````

### Vessels

````python

my_vessel = fleet[0]
# or
my_vessel = fm.vessel(mmsi='239725000')
# or
my_vessel = fm.vessel(imo='9197545')
# or
my_vessel = fm.vessel(name='MINNOW')

# Passing incomplete information will raise an error
my_vessel = fm.vessel()
# ValueError

my_vessel.name
# SS MINNOW

my_vessel.navigationstatus
# On a three hour tour

my_vessel.etatime
# datetime.datetime(1964, 9, 26, 12, 0, tzinfo=<UTC>)

my_vessel.coords
# (3.469557, -167.255859)

# Missing attributes return None
my_vessel.location
# None

````

Minimum list of `Vessel` attributes:

* `coords` (lat, lon)
* `course`
* `destination`
* `draught`
* `etatime`
* `flag`
* `heading`
* `imonumber`
* `last_port`
* `latitude`
* `location`
* `longitude`
* `mmsinumber`
* `name`
* `navigationstatus`
* `photos`
* `positionreceived`
* `publicurl`
* `speed`
* `type`

### Ports

````python

my_vessel.last_port
# <fleetmonger.port.Port object>

port = my_vessel.last_port

port.name
# 'Honolulu, HI'

port.duration
# datetime.timedelta(...)

````
### Port urls and Vessel urls

In general, the parameters that Fleetmonger expects match those of the Fleetmon API, with the following exceptions:

```
instead of mmsinumber, use mmsi
...        imonumber   ... imo
...        q           ... name
```

````python
fm.vesselurl(name='MINNOW')

fm.porturl(locode='USLAX')

fm.vesselurl(locode='USLAX')
````

### Weather at Location

````python
fm.weather(lat=3.469557, lon=-167.255859)

# You can also pass a vessel object to the weather call
fm.weather(vessel=my_vessel)
````
