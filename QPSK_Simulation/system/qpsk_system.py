import numpy as np
from modulation.qpsk import QPSK
from channel.rayleigh_awgn import RayleighAWGNChannel
from estimation.lse_estimator import LSEEstimator

class QPSKSystem:
    """Simulates QPSK communication system with LSE-based equalization."""

    def __init__(self, numFrames=2000, bitsPerFrame=1024, SNR_dB=None):
        self.numFrames = numFrames
        self.bitsPerFrame = bitsPerFrame
        self.SNR_dB = np.arange(0, 22, 2) if SNR_dB is None else np.array(SNR_dB)
        self.modulator = QPSK()
        self.channel = RayleighAWGNChannel()
        self.estimator = LSEEstimator()
        self._create_pilot()

    def _create_pilot(self):
        lts = np.array([1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1,
                        -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 0, 1, -1, -1,
                        1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1,
                        -1, 1, -1, 1, -1, 1, 1, 1, 1])
        ts = np.concatenate([lts, lts])
        self.txPilot = ts.astype(complex)
        self.Np = len(self.txPilot)

    def run(self):
        np.random.seed(0)
        BER = np.zeros_like(self.SNR_dB, dtype=float)

        for si, snr_db in enumerate(self.SNR_dB):
            snr_linear = 10 ** (snr_db / 10)
            errors = 0
            totalBits = 0

            for _ in range(self.numFrames):
                dataBits = np.random.randint(0, 2, self.bitsPerFrame)
                dataSymbols = self.modulator.bits2symbols(dataBits)
                txSymbols = np.concatenate([self.txPilot, dataSymbols])

                h = self.channel.rayleigh()
                rxSymbols = h * txSymbols
                rxSymbols = self.channel.add_awgn(rxSymbols, snr_linear)

                h_est = self.estimator.estimate(rxSymbols[:self.Np], self.txPilot)
                eqData = rxSymbols[self.Np:] / h_est

                detectedSymbols = self.modulator.nearest_point(eqData)
                detectedBits = self.modulator.symbols2bits(detectedSymbols)
                errors += np.sum(dataBits[:len(detectedBits)] != detectedBits)
                totalBits += len(dataBits)

            BER[si] = errors / totalBits
            print(f"SNR={snr_db:2d} dB → BER={BER[si]:.5e} (errors={errors})")

        self.BER = BER
        return BER
