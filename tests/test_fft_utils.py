
import numpy as np

from src.bb_utils.fft_utils import stft



def test_stft():
    win_size = 1024
    hop_size = 256
    p = win_size

    x = np.arange(win_size * 5)

    spec = stft(x, win_size, hop_size, p=p, win=np.hamming(win_size))

    num_freqs = (win_size + p) // 2 + 1
    num_frames = 17 # spec.shape[1]

    assert spec.shape == (num_freqs, num_frames)
    assert spec[0, 0] == 282603.75 + 0j
    assert spec[-1, -1] == -40.95999783091247 + 0j



if __name__ == "__main__":
    test_stft()
