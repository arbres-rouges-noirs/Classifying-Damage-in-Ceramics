import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing
from scipy.stats import iqr
def label():
    file_location = "C:\\Users\\speak\\OneDrive\\Documents\\Documentos\\Programming\\Python\\Research\\Feature_Extraction\\Final_Version\\Raw_Data.xlsx"
    df = pd.read_excel(file_location, usecols="D,E")
    df = df.dropna()
    width, depth = df['Largura do corte (mm)'], df['Profundidade do corte (µm)']
    area = np.multiply(width, depth)

    area_q1 = np.percentile(area, 25)
    area_q3 = np.percentile(area, 75)
    area_iqr = iqr(area)
    area_quartile_deviation = area_iqr/2
    #data_area = [area_q1, area_q3, area_iqr, area_quartile_deviation]
    #df_width = pd.DataFrame(data_width, columns=['1st_Q', '3rd_Q', 'IQR', 'QUARTILE_DEVIATION'])

    #data_depth = [[depth_q1, depth_q3, depth_iqr, depth_quartile_deviation]]
    #depth_dict = {'1st Q': {depth_q1}, '3rd Q': {depth_q3}, 'IQR' : {depth_iqr}, 'Quartile Deviation' : {depth_quartile_deviation} }
    #df_depth = pd.DataFrame(data_depth, columns=['1st_Q', '3rd_Q', 'IQR', 'QUARTILE_DEVIATION'])
    shape = width.shape
    dmg = []
    #print(shape)
    for row in range(shape[0]):
        if area[row] <= area_q1:
            dmg.append(0) #Low damage
        if area[row] > area_q1 and area[row] < area_q3:
            dmg.append(1) #Average damage
        if area[row] >= area_q3:
            dmg.append(2) #High damage

    return dmg