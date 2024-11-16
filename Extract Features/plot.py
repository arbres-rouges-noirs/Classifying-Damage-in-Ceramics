import pandas as pd
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np


dict = loadmat('ensaios.mat')
values = np.array(dict.get("Ensaio01_ch3"))
plt.ylabel('Volts (V)')
plt.xlabel('No. of Samples')
plt.plot(values)
plt.show()