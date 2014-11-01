from .vessel import vessel

class vessel_wrapper(list):
    """contain list of vessels"""

    def __init__(self, kwargs):
        super(vessel_wrapper, self).__init__()

        self.meta = kwargs['meta']
        vessels = kwargs['objects']

        for vdict in vessels:
            _v = vdict['vessel']
            self.append(vessel(_v))
