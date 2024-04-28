#importing the necessary libraries and dependencies
import pandas as pd
import numpy as np
import glob
import os
import random 
import requests
# For Data Preprocessing
from sklearn.preprocessing import MinMaxScaler ,LabelEncoder, StandardScaler
from sklearn import preprocessing

# For building the LSTM Model
from numpy import array

from keras.models import model_from_json

from flask import Flask, render_template,request , url_for, redirect,session
# from Tree import tree
    # Load PM2.5 the jasom model
    # Load PM2.5 the jasom model
PM25_file = open("C:\\Users\\hp\\Desktop\\GPF\\PM25_model.json", 'r')
PM25_loaded_model_json = PM25_file.read()
PM25_loaded_model = model_from_json(PM25_loaded_model_json)
PM25_loaded_model.load_weights("C:\\Users\\hp\\Desktop\\GPF\\PM25_model.h5")

        #Load PM10 model
PM10_file = open("C:\\Users\\hp\\Desktop\\GPF\\PM10_model.json", 'r')
PM10_loaded_model_json = PM10_file.read()
PM10_loaded_model = model_from_json(PM10_loaded_model_json)
PM10_loaded_model.load_weights("C:\\Users\\hp\\Desktop\\GPF\\PM10_model.h5")

        #Load NO2 model
NO2_file = open("C:\\Users\\hp\\Desktop\\GPF\\NO2_model.json", 'r')
NO2_loaded_model_json = NO2_file.read()
NO2_loaded_model = model_from_json(NO2_loaded_model_json)
NO2_loaded_model.load_weights("C:\\Users\\hp\\Desktop\\GPF\\NO2_model.h5")

        #Load CO model
CO_file = open("C:\\Users\\hp\\Desktop\\GPF\\CO_model.json", 'r')
CO_loaded_model_json = CO_file.read()
CO_loaded_model = model_from_json(CO_loaded_model_json)
CO_loaded_model.load_weights("C:\\Users\\hp\\Desktop\\GPF\\CO_model.h5")

        #Load O3 model
O3_file = open("C:\\Users\\hp\\Desktop\\GPF\\O3_model.json", 'r')
O3_loaded_model_json = O3_file.read()
O3_loaded_model = model_from_json(O3_loaded_model_json)
O3_loaded_model.load_weights("C:\\Users\\hp\\Desktop\\GPF\\O3_model.h5")

        #Load TEMP model
TEMP_file = open("C:\\Users\\hp\\Desktop\\GPF\\TEMP_model.json", 'r')
TEMP_loaded_model_json = TEMP_file.read()
TEMP_loaded_model = model_from_json(TEMP_loaded_model_json)
TEMP_loaded_model.load_weights("C:\\Users\\hp\\Desktop\\GPF\\TEMP_model.h5")
def Predict21():
    num = 4
    count = 0
    df = pd.read_csv("C:\\Users\\hp\\Desktop\\GPF\\DATA1.csv")
    # Set the index to the timestamp of the row
    df.index = pd.to_datetime(df[['year', 'month', 'day', 'hour']], format='%Y %m %d %H')
    df.index.name='date'
    df = df.drop(columns=[ 'PRES', 'DEWP', 'RAIN', 'wd', 'WSPM','No', 'year', 'month', 'day', 'hour', 'SO2'])
## Replace the null value with average
    x = df["PM2.5"].median()
    df["PM2.5"].fillna(x, inplace = True)
    x = df["PM10"].median()
    df["PM10"].fillna(x, inplace = True)
    x = df["NO2"].median()
    df["NO2"].fillna(x, inplace = True)
    x = df["CO"].median()
    df["CO"].fillna(x, inplace = True)
    x = df["O3"].median()
    df["O3"].fillna(x, inplace = True)
    x = df["TEMP"].median()
    df["TEMP"].fillna(x, inplace = True)
    df= df.dropna()
    
    while count < num:
        #PM2.5 PREDICT
        PM25values = df.values
        scaler = MinMaxScaler(feature_range=(0, 1))
        PM25data = scaler.fit_transform(PM25values)
        PM25data = PM25data.reshape((PM25data.shape[0], 1, PM25data.shape[1]))
        PM25predict = PM25_loaded_model.predict(PM25data)
        PM25redata = PM25data.reshape((PM25data.shape[0], PM25data.shape[2]))
        PM25 = np.concatenate((PM25predict, PM25redata[:, 1:]), axis=1)
        # invert scale the concatenated data for forecast
        predictedPM25 = scaler.inverse_transform(PM25)
        predictedPM25 = pd.DataFrame(predictedPM25, columns=df.columns)
        predictedPM25 = predictedPM25.round(2)
        df_last_row = predictedPM25.tail(1)
        P_PM25 = df_last_row['PM2.5'].values[0]

        #PM10 PREDICT
        new_cols = ["PM10", "PM2.5", "NO2", "CO", "O3", "TEMP", "station"]
        df2=df.reindex(columns=new_cols)
        PM10values = df2.values
        scaler = MinMaxScaler(feature_range=(0, 1))
        PM10data = scaler.fit_transform(PM10values)
        PM10data = PM10data.reshape((PM10data.shape[0], 1, PM10data.shape[1]))
        PM10predict = PM25_loaded_model.predict(PM10data)
        PM10redata = PM10data.reshape((PM10data.shape[0], PM10data.shape[2]))
        PM10 = np.concatenate((PM10predict, PM10redata[:, 1:]), axis=1)
        # invert scale the concatenated data for forecast
        predictedPM10 = scaler.inverse_transform(PM10)
        predictedPM10 = pd.DataFrame(predictedPM10, columns=df2.columns)
        predictedPM10 = predictedPM10.round(2)
        df_last_row = predictedPM10.tail(1)
        P_PM10 = df_last_row['PM10'].values[0]

        #NO2 PREDICT
        new_cols = ["NO2", "PM2.5", "PM10",  "CO", "O3", "TEMP", "station"]
        df3 = df.reindex(columns = new_cols)
        NO2values = df3.values
        scaler = MinMaxScaler(feature_range=(0, 1))
        NO2data = scaler.fit_transform(NO2values)
        NO2data = NO2data.reshape((NO2data.shape[0], 1, NO2data.shape[1]))
        NO2predict = NO2_loaded_model.predict(NO2data)
        NO2redata = NO2data.reshape((NO2data.shape[0], NO2data.shape[2]))
        NO2 = np.concatenate((NO2predict, NO2redata[:, 1:]), axis=1)
        # invert scale the concatenated data for forecast
        predictedNO2 = scaler.inverse_transform(NO2)
        predictedNO2 = pd.DataFrame(predictedNO2, columns=df3.columns)
        predictedPM10 = predictedPM10.round(2)
        df_last_row = predictedPM10.tail(1)
        P_NO2 = df_last_row['NO2'].values[0]

        #CO PREDICT
        new_cols = ["CO", "PM2.5", "PM10",  "NO2", "O3", "TEMP", "station"]
        df4=df.reindex(columns=new_cols)
        COvalues = df4.values
        scaler = MinMaxScaler(feature_range=(0, 1))
        COdata = scaler.fit_transform(COvalues)
        COdata = COdata.reshape((COdata.shape[0], 1, COdata.shape[1]))
        COpredict = CO_loaded_model.predict(COdata)
        COredata = COdata.reshape((COdata.shape[0], COdata.shape[2]))
        CO = np.concatenate((COpredict, COredata[:, 1:]), axis=1)
        # invert scale the concatenated data for forecast
        predictedCO = scaler.inverse_transform(CO)
        predictedCO = pd.DataFrame(predictedCO, columns=df4.columns)
        predictedCO = predictedCO.round(2)
        df_last_row = predictedCO.tail(1)
        P_CO = df_last_row['CO'].values[0]

        #O3 PREDICT
        new_cols = ["O3", "PM2.5", "PM10",  "NO2", "CO", "TEMP", "station"]
        df5=df.reindex(columns=new_cols)
        O3values = df5.values
        scaler = MinMaxScaler(feature_range=(0, 1))
        O3data = scaler.fit_transform(O3values)
        O3data = O3data.reshape((O3data.shape[0], 1, O3data.shape[1]))
        O3predict = O3_loaded_model.predict(O3data)
        O3redata = O3data.reshape((O3data.shape[0], O3data.shape[2]))
        O3 = np.concatenate((O3predict, O3redata[:, 1:]), axis=1)
        # invert scale the concatenated data for forecast
        predictedO3 = scaler.inverse_transform(O3)
        predictedO3 = pd.DataFrame(predictedO3, columns=df5.columns)
        predictedO3 = predictedO3.round(2)
        df_last_row = predictedO3.tail(1)
        P_O3 = df_last_row['O3'].values[0]

        #TEMP PREDICT
        new_cols = ["TEMP", "PM2.5", "PM10", "NO2", "CO", "O3", "station"]
        df6=df.reindex(columns=new_cols)
        TEMPvalues = df6.values
        scaler = MinMaxScaler(feature_range=(0, 1))
        TEMPdata = scaler.fit_transform(TEMPvalues)
        TEMPdata = TEMPdata.reshape((TEMPdata.shape[0], 1, TEMPdata.shape[1]))
        TEMPpredict = TEMP_loaded_model.predict(TEMPdata)
        TEMPredata = TEMPdata.reshape((TEMPdata.shape[0], TEMPdata.shape[2]))
        TEMP = np.concatenate((TEMPpredict, TEMPredata[:, 1:]), axis=1)
        # invert scale the concatenated data for forecast
        predictedTEMP = scaler.inverse_transform(TEMP)
        predictedTEMP = pd.DataFrame(predictedTEMP, columns=df6.columns)
        predictedTEMP = predictedTEMP.round(2)
        df_last_row = predictedTEMP.tail(1)
        P_TEMP = df_last_row['TEMP'].values[0]

        df.loc[len(df.index)] = [P_PM25, P_PM10, P_NO2, P_CO, P_O3, P_TEMP, 13]

        def cal_PM25I(PM25):
                PM25I=0
                if(PM25<=30):
                    PM25I= PM25*50/30
                elif(PM25>30 and PM25<=60):
                    PM25I= 50+(PM25-30)*(50/30)
                elif(PM25>60 and PM25<=90):
                    PM25I= 100+(PM25-60)*(100/30)
                elif(PM25>90 and PM25<=120):
                    PM25I= 200+(PM25-90)*(100/30)
                elif(PM25>120 and PM25<=250):
                    PM25I= 300+(PM25-120)*(100/130)
                elif(PM25>250):
                    PM25I= 400+(PM25-250)*(100/130)
                return PM25I
        df['PM25I'] = df['PM2.5'].apply(cal_PM25I)

        def cal_PM10I(PM10):
                PM10I=0
                if(PM10<=50):
                    PM10I= PM10
                elif(PM10>50 and PM10<=100):
                    PM10I= PM10
                elif(PM10>100 and PM10<=250):
                    PM10I= 100+(PM10-100)*(100/150)
                elif(PM10I>250 and PM10<=350):
                    PM10I= 200+(PM10-250)
                elif(PM10>350 and PM10<=430):
                    PM10I= 300+(PM10-350)*(100/80)
                elif(PM10>430):
                    PM10I= 400+(PM10-430)*(100/80)
                return PM10I
        df['PM10I']= df['PM10'].apply(cal_PM10I)

        def cal_NO2I(NO2):
                NO2I=0
                if(NO2<=40):
                    NO2I= NO2*50/40
                elif(NO2>40 and NO2<=80):
                    NO2I= 50+(NO2-40)*(50/40)
                elif(NO2>80 and NO2<=180):
                    NO2I= 100+(NO2-80)*(100/100)
                elif(NO2>180 and NO2<=280):
                    NO2I= 200+(NO2-180)*(100/100)
                elif(NO2>280 and NO2<=400):
                    NO2I= 300+(NO2-280)*(100/120)
                else:
                    NO2I= 400+(NO2-400)*(100/120)
                return NO2I
        df['NO2I']= df['NO2'].apply(cal_NO2I)

        def cal_COI(CO):
                COI=0
                if(CO<=1):
                    COI= CO*(50/1)
                elif(CO>1 and CO<=2):
                    COI= 50+(CO-1)*50/1
                elif(CO>2 and CO<=10):
                    COI= 100+(CO-2)*(100/8)
                elif(CO>10 and CO<=17):
                    COI= 200+(CO-10)*(100/7)
                elif(CO>17 and CO<=34):
                    COI= 300+(CO-17)*(100/17)
                elif(CO>34):
                    COI= 400+(CO-34)*(100/17)
                return COI
        df['COI']= df['CO'].apply(cal_COI)

        def cal_O3I(O3):
                O3I=0
                if(O3<=50):
                    O3I= O3*(50/50)
                elif(O3>50 and O3<=100):
                    O3I= 50+(O3-50)*50/50
                elif(O3>2 and O3<=168):
                    O3I= 100+(O3-100)*(100/68)
                elif(O3>168 and O3<=208):
                    O3I= 200+(O3-168)*(100/40)
                elif(O3>208 and O3<=748):
                    O3I= 300+(O3-208)*(100/539)
                elif(O3>748):
                    O3I= 400+(O3-400)*(100/539)
                return O3I
        df['O3I']= df['O3'].apply(cal_O3I)

        def cal_AQI(PM25I,PM10I,NO2I,COI,O3I):
                AQI=0
                if(PM25I>PM10I and PM25I>NO2I and PM25I>COI and PM25I>O3I):
                    AQI= PM25I
                elif(PM10I>PM25I and PM10I>NO2I and PM10I>COI and PM10I>O3I):
                    AQI= PM10I
                elif(NO2I>PM25I and NO2I>PM10I  and NO2I>COI and NO2I>O3I):
                    AQI= NO2I
                elif(COI>PM25I and COI>PM10I and COI>NO2I and COI>O3I):
                    AQI= COI
                elif(O3I>PM25I and O3I>PM10I  and O3I>NO2I and O3I>COI):
                    AQI= O3I
                return AQI
        df['AQI']= df.apply(lambda x:cal_AQI(x['PM25I'], x['PM10I'], x['NO2I'], x['COI'], x['O3I']),axis=1)

        def AQI_Range(x):
                if(x<=50):
                    return "Good"
                elif(x>50 and x<=100):
                    return "Moderate"
                elif(x>100 and x<=200):
                    return "Poor"
                elif(x>200 and x<=300):
                    return "Unlealthy"
                elif(x>300 and x<=400):
                    return "Very Unlealthy"
                elif(x>400):
                    return "Hazardous"
        df['AQI_Range'] = df['AQI'].apply(AQI_Range)
        P_AQI = df['AQI_Range'].values[0] 

        df = df.drop(columns=['AQI_Range', 'AQI', 'PM25I', 'PM10I', 'NO2I', 'COI', 'O3I'])
        count = count + 1   
    return (P_PM25 , P_PM10 , P_NO2 , P_CO , P_O3 , P_AQI )
     

def SENDP11():
  P_PM25,P_PM10,P_NO2 ,P_CO,P_O3,P_AQI=Predict21()
  return (P_PM25 , P_PM10 , P_NO2 , P_CO , P_O3 , P_AQI )
