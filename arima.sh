#!/bin/sh
# arima.sh

sleep 100

cd /
cd home/pi/Desktop/arima
while :
do 
    	sudo python py_query.py
	sleep 60
	sudo python py_collected_pred.py
	sleep 30
done
cd/

