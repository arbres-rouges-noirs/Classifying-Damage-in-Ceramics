from scipy.fft import fft, rfft, fftfreq, rfftfreq
from scipy.linalg import dft
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pandas as pd

#Fazer dar certo

data = dict.get('EnsaioREC08_ch3')

sample_rate = 1000000
duration = 0.625
no_samples = int(sample_rate*duration)
yf = rfft(data)
xf = rfftfreq(no_samples, 1/sample_rate)

plt.plot(np.abs(yf))
plt.show()