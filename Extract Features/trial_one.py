import numpy as np
import statsmodels as stats
from scipy.fft import fft
import pandas as pd
from scipy.stats import kurtosis, skew


def feat(X): 
    signal_features = []
    
    Min=[];Max=[];Mean=[];Rms=[];Var=[];Std=[];Power=[];Peak=[];Skew=[];Kurtosis=[];P2p=[];CrestFactor=[];
    FormFactor=[]; PulseIndicator=[];
    Max_f=[];Sum_f=[];Mean_f=[];Var_f=[];Peak_f=[];Skew_f=[];Kurtosis_f=[]
    
    #X = df.values
    ## TIME DOMAIN ##
    signal_features.append(np.max(X))
    signal_features.append(np.min(X))
    signal_features.append(np.mean(X))
    signal_features.append(np.sqrt(np.mean(X**2)))
    signal_features.append(np.var(X))
    signal_features.append(np.std(X))
    signal_features.append(np.mean(X**2))
    signal_features.append(np.max(np.abs(X)))
    signal_features.append(np.ptp(X))
    signal_features.append(np.max(np.abs(X))/np.sqrt(np.mean(X**2)))
    signal_features.append(np.sqrt(np.mean(X**2))/np.mean(X))
    signal_features.append(np.max(np.abs(X))/np.mean(X))
    ## FREQ DOMAIN ##
    ft = fft(X)
    S = np.abs(ft**2)/17
    signal_features.append(np.max(S))
    signal_features.append(np.sum(S))
    signal_features.append(np.mean(S))
    signal_features.append(np.var(S))
    signal_features.append(np.max(np.abs(S)))
    print(np.array(signal_features).shape)

    #print(len(signal_features))
    #Create dataframe from features
    '''df_features = pd.DataFrame(index = [FEATURES], 
                               data = [Min,Max,Mean,Rms,Var,Std,Power,Peak,P2p,CrestFactor,Skew,Kurtosis,
                                       Max_f,Sum_f,Mean_f,Var_f,Peak_f,Skew_f,Kurtosis_f])'''
    return signal_features

