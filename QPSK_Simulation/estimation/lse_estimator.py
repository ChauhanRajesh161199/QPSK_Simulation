import numpy as np

class LSEEstimator:
    """Least Squares Estimation (LSE) for flat fading channel."""

    @staticmethod
    def estimate(rxPilot, txPilot):
        denom = np.sum(np.abs(txPilot) ** 2)
        if denom == 0:
            return np.sum(np.conj(txPilot) * rxPilot) / (np.sum(np.abs(txPilot) > 0) + np.finfo(float).eps)
        return np.sum(np.conj(txPilot) * rxPilot) / denom
