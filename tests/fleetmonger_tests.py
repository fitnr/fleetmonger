from fleetmonger import Fleetmonger
import unittest

class FleetMongerTestCase(unittest.TestCase):

    def setUp(self):
        user, key = '', ''
        self.f = Fleetmonger(user, key)

    def test_fleet(self):
        fleet = self.f.myfleet()
        assert fleet
        assert len(fleet) > 0

if __name__ == '__main__':
    unittest.main()
