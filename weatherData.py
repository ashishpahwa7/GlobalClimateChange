import csv
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def read_dates(file_name):
    dates = np.genfromtxt(file_name,delimiter = ",",skip_header=0,dtype=str,filling_values='null',usecols=(0,1) )
    dates = dates[1:,0]
    dates_list = [dt.datetime.strptime(date, '%Y-%m-%d').date() for date in dates]
    return dates_list
    

def read_LandAvgTemp(file_name):
    lat = np.genfromtxt(file_name,delimiter = ",",skip_header=0,dtype=str,filling_values='null',usecols=(0,1) )
    lat = lat[1:,1]
    return lat


def clean_data(dates_list,lat):  
    dump = np.nonzero(lat=='')[0]
    dates_list = np.delete(dates_list,dump,axis=0)
    lat = np.delete(lat,dump,axis=0)
    return (dates_list,lat)


def sort_by_month(dates_list,lat,month):
    month_index=[]
    for i in range(0,len(dates_list)-1):
        if(dates_list[i].month==month):
            month_index.append(i)
    
    return month_index
       

def plot_by_month(X,Y,month):
    month_index=sort_by_month(dates_list,lat,month)
    temp_month=[]
    temp_lat=[]
    for index in month_index:
        temp_month.append(dates_list[index])
        temp_lat.append(lat[index])
    X = temp_month
    Y = temp_lat
    plt.plot(X,Y)
    plt.xlabel(set_month(month),fontsize=20)
    plt.ylabel('Avg Temperature')
    plt.savefig('test.jpg')
    plt.show()


def set_month(month):
    year = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    set = year[month-1]
    return set
                        
dates_list=read_dates('GlobalTemperatures.csv')
lat=read_LandAvgTemp('GlobalTemperatures.csv')
dates_list,lat = clean_data(dates_list,lat)
lat=lat.astype(float)
X=dates_list
Y=lat
for month in range(1,13):
    plot_by_month(X,Y,month)





