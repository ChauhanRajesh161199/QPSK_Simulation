import numpy as np

class Modulation:
    """Base class for digital modulation schemes."""
    def bits2symbols(self, bits):
        raise NotImplementedError

    def symbols2bits(self, symbols):
        raise NotImplementedError

    def nearest_point(self, rxSymbols):
        raise NotImplementedError