import numpy as np

class RayleighAWGNChannel:
    """Models Rayleigh fading + AWGN noise channel."""

    @staticmethod
    def rayleigh():
        return (np.random.randn() + 1j * np.random.randn()) / np.sqrt(2)

    @staticmethod
    def add_awgn(signal, snr_linear):
        Es = 1
        noiseVar = Es / snr_linear
        sigma = np.sqrt(noiseVar / 2)
        noise = sigma * (np.random.randn(len(signal)) + 1j * np.random.randn(len(signal)))
        return signal + noise
