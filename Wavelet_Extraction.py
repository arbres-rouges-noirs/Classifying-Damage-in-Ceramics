import pywt
import numpy as np
import os
from scipy.io import loadmat
import pandas as pd
import matplotlib.pyplot as plt
#fazer dar certo
#estudar mais wavelet

dict = loadmat('EnsaioREC08_ch3.mat')
del dict['__header__'], dict['__version__'], dict['__globals__']

data = dict.get('EnsaioREC08_ch3')
dim = data.shape
wave = pywt.dwt(data, 'db1')
max_level = pywt.dwt_max_level(dim[0], 'db1')
coeffs = pywt.wavedec(data, 'db1', level=5)
plt.plot(coeffs[0], color='blue',label='after')
#plt.plot(data, color='red',label='before')

plt.show()

'''for row in wave:
    plt.plot(row)
    plt.show()'''


