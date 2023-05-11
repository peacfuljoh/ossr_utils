
import os

import numpy as np

from src.bb_utils.audio_utils import read_wav, write_wav



def test_read_write_wav():
    fname = './dummy.wav'
    n = 100
    x = np.arange(n)
    x = x.astype('int16') # just in case
    sr = 44100
    write_wav(fname, sr, x)
    sr_read, x_read = read_wav(fname)
    os.remove(fname)
    assert np.allclose(x_read, x)



if __name__ == "__main__":
    test_read_write_wav()