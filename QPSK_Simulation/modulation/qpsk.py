import numpy as np
from .modulation_base import Modulation

class QPSK(Modulation):
    """Implements QPSK modulation and demodulation."""

    def __init__(self):
        self.constellation = np.array([1+1j, 1-1j, -1+1j, -1-1j]) / np.sqrt(2)

    def bits2symbols(self, bits):
        bits = np.array(bits)
        if len(bits) % 2 != 0:
            bits = bits[:-1]
        symbols = []
        for i in range(0, len(bits), 2):
            real_part = 1 - 2 * bits[i]
            imag_part = 1 - 2 * bits[i+1]
            symbols.append((real_part + 1j * imag_part) / np.sqrt(2))
        return np.array(symbols)

    def nearest_point(self, rxSymbols):
        decided = []
        for sym in rxSymbols:
            real_part = 1 if np.real(sym) >= 0 else -1
            imag_part = 1 if np.imag(sym) >= 0 else -1
            decided.append((real_part + 1j * imag_part) / np.sqrt(2))
        return np.array(decided)

    def symbols2bits(self, symbols):
        bits = []
        for sym in symbols:
            bits.append(int((1 - np.sign(np.real(sym))) / 2))
            bits.append(int((1 - np.sign(np.imag(sym))) / 2))
        return np.array(bits, dtype=int)
