from scipy.io import loadmat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ExtractFeatures
import csv
import numpy as np

# Abrindo o arquivo com os dados
dict = loadmat('ensaios.mat')
del dict['__header__'], dict['__version__'], dict['__globals__']
#cols = ['IsStationary', 'No. of Peaks', 'Autocov', 'Seasonality', 'Amplitude']

filename = 'testes_laser.csv'

with open(filename,'w',newline='') as file:
    writer = csv.writer(file)
    cols = ['IsStationary','No. of Peaks']
    writer.writerow(cols)
    for item in dict.values():
        features = []
        ts = np.reshape(item, -1)
        features.append(ExtractFeatures.adfuller(ts))
        features.append(ExtractFeatures.No_Peaks(ts))
        writer.writerow(features)

print(filename)