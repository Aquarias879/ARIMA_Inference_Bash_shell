from influxdb import DataFrameClient
import numpy as np
import pandas as pd
import time
from datetime import datetime
import datetime
from py_in import temp_p,hum_p,soil_p,ec_p
import pytz

host = '203.64.131.98'
port = 8086
user = 'sam'
password = '12345678'
protocol='line'
dbname = 'Predicted'

client = DataFrameClient(host, port, user, password, dbname)

now = datetime.datetime.now(pytz.timezone('Asia/Taipei'))
dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
time_tz = pd.date_range(dt_string,periods=30 ,freq = 'T')
time=pd.DataFrame({'time': pd.to_datetime(time_tz),})
df_temp = pd.concat([time, temp_p], axis=1)
df_hum = pd.concat([time, hum_p], axis=1)
df_soil = pd.concat([time, soil_p], axis=1)
df_ec = pd.concat([time, ec_p], axis=1)
df_temp.index  = pd.to_datetime(df_temp['time'])
df_hum.index  = pd.to_datetime(df_hum['time'])
df_soil.index  = pd.to_datetime(df_soil['time'])
df_ec.index  = pd.to_datetime(df_ec['time'])
df_temp['time'] = pd.to_datetime(df_temp.index, unit='ns').astype(np.int64) // 10**9
df_hum['time'] = pd.to_datetime(df_hum.index, unit='ns').astype(np.int64) // 10**9
df_soil['time'] = pd.to_datetime(df_soil.index, unit='ns').astype(np.int64) // 10**9
df_ec['time'] = pd.to_datetime(df_ec.index, unit='ns').astype(np.int64) // 10**9
client.write_points(
    df_temp,
    "temp_pred",
  )
client.write_points(
    df_hum,
    "hum_pred",
  )
client.write_points(
    df_soil,
    "soil_pred",
  )
client.write_points(
    df_ec,
    "ec_pred",
  )
print ("finished !!")
    



