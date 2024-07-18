import statsmodels
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
from statsmodels.tsa.stattools import acovf, acf
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from scipy.signal import argrelextrema

#Find if it's Stationary or not
#Data used here must be 1-d Array (use to_numpy)
def IsStationary(data):
    print("oii")
    #read the spreadsheet from the google drive
    result = adfuller(data)
    #write new data accordingly to the results of the test
    if result[1] < 0.5:
      return True
    else:
      return False


#Find the number of peaks in each dataserie
#Data used here must be 1-d Array (use to_numpy)
def No_Peaks(item):
  peaks, _ = find_peaks(item, height=0)
  #plt.plot(x)
  dim = peaks.shape
  return dim[0]
  #plt.plot(peaks, x[peaks], "x")
  #plt.plot(np.zeros_like(x), "--", color="gray")
  #plt.show()


#Data used here must be Ndarray
def FindAutocov(data):
 i=0

#Data used here must be Ndarray
def FindAutoCor(data):
  i = 0

#Data used here must be DataFrame from pandas
def isSeasonalAditive(data):
  return True

def isSeasonalMultiplicative(data):
  return True

def LocalMax(data):
  #x = np.random.random(12) #timeseries that should be in 1-D array
# for local maxima
  data[argrelextrema(data, np.greater)[0]]

def LocalMin(data):
 #timeseries that should be in 1-D array
  # for local minima
  data[argrelextrema(data, np.less)[0]]
