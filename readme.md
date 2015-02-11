## Fleetmonger

Python wrapper for the [fleetmon.com](fleetmon.com) ship-tracking API.

## API Calls
[Read the details of the API at Fleetmonger](https://www.fleetmon.com/faq/public_api).
* fleetmonger.vessel
* fleetmonger.vesselparticulars
* fleetmonger.vesselurl
* fleetmonger.porturl
* fleetmonger.weather_at_position

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
