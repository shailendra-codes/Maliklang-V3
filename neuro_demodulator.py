import numpy as np
from scipy.signal import butter, lfilter

class NeuroDemodulator:
    def __init__(self, sample_rate=256):
        self.sample_rate = sample_rate

    def bandpass_filter(self, data, lowcut=0.5, highcut=50.0, order=5):
        nyquist = 0.5 * self.sample_rate
        low = lowcut / nyquist
        high = highcut / nyquist
        b, a = butter(order, [low, high], btype='band')
        return lfilter(b, a, data)

    def clean_signal(self, raw_eeg_signals):
        """
        Removes ocular (blinking) and muscular noise matrix from raw channels.
        """
        cleaned_matrix = {}
        for channel, signal in raw_eeg_signals.items():
            np_signal = np.array(signal, dtype=np.float64)
            filtered = self.bandpass_filter(np_signal)
            # Remove high-frequency muscle spikes
            cleaned_matrix[channel] = np.clip(filtered, -100.0, 100.0).tolist()
        return cleaned_matrix
 
