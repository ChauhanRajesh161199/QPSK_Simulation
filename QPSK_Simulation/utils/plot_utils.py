import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc

def plot_ber(SNR_dB, BER, title="QPSK BER vs SNR"):
    theory = 0.5 * erfc(np.sqrt(10 ** (SNR_dB / 10)))
    plt.figure(figsize=(8, 5))
    plt.semilogy(SNR_dB, BER, '-o', label='Simulated (Rayleigh + LSE)')
    plt.semilogy(SNR_dB, theory, '--', label='Theoretical AWGN QPSK')
    plt.xlabel('SNR (dB)')
    plt.ylabel('Bit Error Rate (BER)')
    plt.title(title)
    plt.grid(True, which='both')
    plt.legend()
    plt.ylim([1e-5, 1])
    plt.show()
