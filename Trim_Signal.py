import pandas as pd
import openpyxl
from scipy.fft import fft, rfft, fftfreq, rfftfreq
from scipy.linalg import dft
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pandas as pd

#required_cols = [0,2]
dict = loadmat('ensaios.mat')
parameters = openpyxl.load_workbook('Dataset_Parameters.xlsx')
damage_len = 5.
sample_no = 1000000

del dict['__header__'], dict['__version__'], dict['__globals__']
sample = parameters.worksheets[0]
#olhar posicao 6 e 7
teste = 0
count = 0
for row in sample:
    if teste <= 9:
        ary = np.empty(100)
        if count <= 8 and count > 0:
            num = int((row[0].value))
            sample_id = " "
            if num < 10:
                sample_id = f"Ensaio0{num}_ch3"
            else:
                sample_id = f"Ensaio{num}_ch3"

            ary = np.reshape(dict.get(sample_id), -1)
            peaks, _ = find_peaks(ary, height=0)
            print(peaks)
            first_pos = peaks[0]
            print(first_pos)

            spd = row[2].value
            print(f"Speed = {spd}")

            time = 5/spd
            print(f"Time = {time}")

            signal_len = int((time*sample_no) + first_pos)
            print(f"Signal Length = {signal_len}")
            
            trunc_ary = ary[first_pos:signal_len]
            print(trunc_ary.shape)
        
        count=+1
    else:
        break
    teste+=1