# -*- coding: utf-8 -*-
import openpyxl
from scipy.fft import fft, rfft, fftfreq, rfftfreq
from scipy.linalg import dft
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pandas as pd
from scipy.stats import iqr
from trial_one import feat
from label_data import label
from sklearn.preprocessing import normalize

dict = loadmat('ensaios.mat')
#parameters = openpyxl.load_workbook('Dataset_Parameters.xlsx')
damage_len = 5.
sample_no = 1000000

del dict['__header__'], dict['__version__'], dict['__globals__']
#sample = parameters.worksheets[0]

file_location = "C:\\Users\\speak\\OneDrive\\Documents\\Documentos\\Programming\\Python\\Research\\Feature_Extraction\\Dataset_Parameters.xlsx"
df = pd.read_excel(file_location, usecols="A,C")

sample = pd.DataFrame(df).to_numpy()
dims = sample.shape

data=[]
keys=[]
results = []

#print(f"{shape[0]}, {shape[1]}")

#Skew and Kurtosis, both in time and frequency domains, developed as Nan

FEATURES = ['MIN','MAX','MEAN','RMS','VAR','STD','POWER','PEAK','P2P','CREST FACTOR',
            'FORM FACTOR', 'PULSE INDICATOR', 'MAX_f','SUM_f','MEAN_f','VAR_f','PEAK_f', 'DAMAGE']

for row in range(dims[0]):

    if sample[row][0] < 10:
        sample_id = f"Ensaio0{sample[row][0]}_ch3"
    else:
        sample_id = f"Ensaio{sample[row][0]}_ch3"
    print(sample_id)
    aux = dict.get(sample_id)
    aux_shape = aux.shape
    ary = np.reshape(aux, -1)
    '''
    peaks, _ = find_peaks(ary, height=0)
    first_pos = peaks[0]
    spd = sample[row][1]
    #print(spd)
    time = 5/spd
    signal_len = int((time*sample_no) + first_pos)
    trunc_ary = ary[first_pos:signal_len]'''
    #tuple = ary.shape
    #signal_ary = np.reshape(tary, (-1, tuple[0]))
    features = feat(ary)
    data.append(features)
    


arr = np.array(data)
print(arr.shape)
norm_data = []
for i in range((arr.shape)[1]):
    print(i + 1)
    norm_ary = normalize([arr[:,i]])
    norm_data.append(norm_ary)

result = np.array(label())
print(result.shape)
#features = np.array(norm_data)
norm_data = np.transpose(np.array(norm_data)[:,0,:])
print(norm_data.shape)
#print(f"norm_data = {features.shape} e result = {result.shape}")
features = np.column_stack((norm_data, result))
print(features.shape)
#norm_data = np.hstack((norm_data, result.reshape(-1,1)))
signals = pd.DataFrame(features, columns=FEATURES)
signals.to_csv("C:\\Users\\speak\\OneDrive\\Documents\\Documentos\\Programming\\Python\\Research\\Training_Models\\Models\\ceramic_damage.csv", index=False)

#olhar posicao 6 e 7
