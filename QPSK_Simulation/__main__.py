from system.qpsk_system import QPSKSystem
from utils.plot_utils import plot_ber

if __name__ == "__main__":
    qpsk = QPSKSystem(numFrames=250, bitsPerFrame=1024)
    BER = qpsk.run()
    plot_ber(qpsk.SNR_dB, BER, "BER vs SNR for QPSK (Rayleigh + LSE)")
