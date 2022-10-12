import numpy as np
import pandas as pd
from pmdarima.arima import auto_arima
import pickle
import scipy.signal.signaltools 

temp_dt = pd.read_csv("1temp.csv")
humid_dt = pd.read_csv("1humid.csv")
soil_dt = pd.read_csv("1soil.csv")
ec_dt = pd.read_csv("1ec.csv")
pred_t = []
def temp(pred_t):
    arima_t = auto_arima(temp_dt['last'])
    with open('Temp_model.pkl', 'wb') as pkl1:
        pickle.dump(arima_t, pkl1)
    
    pred_t = arima_t.predict(n_periods=30)
    return pred_t

pred_h = []
def humid(pred_h):
    arima_h = auto_arima(humid_dt['last'])
    with open('Humid_model.pkl', 'wb') as pkl2:
        pickle.dump(arima_h, pkl2)
    
    pred_h = arima_h.predict(n_periods=30)
    return pred_h

pred_s = []
def soil(pred_s):
    arima_s = auto_arima(soil_dt['last'])
    with open('Soil_model.pkl', 'wb') as pkl3:
        pickle.dump(arima_s, pkl3)
    
    pred_s = arima_s.predict(n_periods=30)
    return pred_s

pred_ec = []
def ec(pred_ec):
    arima_ec = auto_arima(ec_dt['last'])
    with open('ec_model.pkl', 'wb') as pkl4:
        pickle.dump(arima_ec, pkl4)
    
    pred_ec = arima_ec.predict(n_periods=30)
    return pred_ec
    
def _centered(arr, newsize):
    # Return the center newsize portion of the array.
    newsize = np.asarray(newsize)
    currsize = np.array(arr.shape)
    startind = (currsize - newsize) // 2
    endind = startind + newsize
    myslice = [slice(startind[k], endind[k]) for k in range(len(endind))]
    return arr[tuple(myslice)]

scipy.signal.signaltools._centered = _centered


predict_temp = temp(pred_t)
predict_hum = humid(pred_h) 
predict_soil = soil(pred_s)
predict_ec = ec(pred_ec)

temp_p = pd.DataFrame(predict_temp)
hum_p = pd.DataFrame(predict_hum)
soil_p = pd.DataFrame(predict_soil)
ec_p = pd.DataFrame(predict_ec)
print("finished !!")
