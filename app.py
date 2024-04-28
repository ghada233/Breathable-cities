
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
from Predict import Predict21,SENDP11
from Predict1 import Predict11,SENDP1
from Predict2 import Predict211,SENDP111
# For building the LSTM Model
from numpy import array
from keras.models import model_from_json
from flask import Flask, render_template ,url_for
# from Tree import tree
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def HomePage():
    return render_template('index.html')
@app.route("/Aboutus")
def Aboutus():
    return render_template('Aboutus.html')
@app.route("/FAQs")
def FAQs():
    return render_template('FAQs.html')

@app.route("/Predict", methods=["GET", "POST"])
def Predict():
    P_PM25,P_PM10,P_NO2 ,P_CO,P_O3,P_AQI=Predict21()
    return render_template('Predict.html', 
                           P_PM25 = P_PM25, P_PM10 = P_PM10, P_NO2 = P_NO2, P_CO = P_CO, P_O3 = P_O3, P_AQI = P_AQI)

@app.route("/RecomendTree" ,methods=["GET", "POST"])
def RecomendTree(): 
 P_PM25,P_PM10,P_NO2 ,P_CO,P_O3,P_AQI=SENDP11()
 # Algorthim PM2.5 recomend 
 if (250.5 <=P_PM25) :
      StatusPM25='hazard'
 elif(105.5<= P_PM25<=250.4) :
      StatusPM25 ="very unhalthey "
 elif ( 55.5<=P_PM25<=150.4) :
      StatusPM25= "unhealthy "          
 elif (35.5<= P_PM25<=55.4) :
      StatusPM25= "unhealthy for sensitive group"  
 elif (12.1<= P_PM25<=35.4) :
      StatusPM25= "Moudrate" 
 elif (0<= P_PM25<=12) :
      StatusPM25= "Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\PM2.5"
 files=os.listdir(path)
 fpic=random.choice(files)
 n= "PM2.5/"+fpic
 NameFpic=fpic.split(".")[0]
 Image_File= url_for('static', filename=n)      
 count=1
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        m2= "PM2.5/"+spic
        NameSpic=spic.split(".")[0]
        Image_File1= url_for('static', filename=m2)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             m3= "PM2.5/"+ tpic 
             NameTpic=tpic.split(".")[0]
             Image_File11= url_for('static', filename=m3)
             count = count + 1
#    End  Algorthim PM2.5 recomend 
# -----------------------------------------------------------------------------
  # Algorthim PM10 recomend 
 if ( 425<= P_PM10) :
      StatusPM10="hazerd"
 elif( 355<= P_PM10<=424) :
       StatusPM10 ="very unhalthey "
 elif( 255<= P_PM10<=354) :
       StatusPM10= "unhealthy "
 elif ( 155<= P_PM10<=254) :
       StatusPM10= "unhealthy for sensitive group"
 elif  ( 55<= P_PM10<=154) :
      StatusPM10 ="Modrate"
 elif  ( 0<= P_PM10<=54) :
      StatusPM10="Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\PM10"
 files=os.listdir(path)
 fpic=random.choice(files)
 PMF= "PM10/"+fpic
 NamePM10PicF=fpic.split(".")[0]
 Image_FilePM10F= url_for('static', filename=PMF)      
 count=1
 noPic=3
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        PMS= "PM10/"+spic
        NamePM10PicS=spic.split(".")[0]
        Image_FilePM10S= url_for('static', filename=PMS)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             PMT= "PM10/"+ tpic 
             NamePM10PicT=tpic.split(".")[0]
             Image_FilePM10T= url_for('static', filename=PMT)
             count = count + 1
  #  End Algorthim PM10 recomend 
# # ---------------------------------
# #    # Algorthim NO2 recomend 
 if ( 1250<= P_NO2) :
     StatusNO ="hazerd "
 elif( 650<= P_NO2<=1249) :
     StatusNO ="very un halthey "
 elif ( 361<= P_NO2<=649) :
     StatusNO= "unhealthy "
 elif (101<= P_NO2<=360) :
     StatusNO= "unhealthy for sensitive group"    
 elif (54<= P_NO2<=100) :
      StatusNO= "Moudrate"
 elif (0<= P_NO2<=53) :
     StatusNO= "Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\NO2"
 files=os.listdir(path)
 fpic=random.choice(files)
 NOF= "NO2/"+fpic
 NameNOPicF=fpic.split(".")[0]
 Image_FileNOF= url_for('static', filename=NOF)      
 count=1
 noPic=3
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        NOS= "NO2/"+spic
        NameNOPicS=spic.split(".")[0]
        Image_FileNOS= url_for('static', filename=NOS)
        count = count + 1
        if count==noPic:
            break
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             NOT= "NO2/"+ tpic 
             NameNOPicT=tpic.split(".")[0]
             Image_FileNOT= url_for('static', filename=NOT)
             count = count + 1
#   #  END Algorthim NO2 recomend
# --------------------------
# #    # Algorthim CO recomend 
 if ( 30.5<=P_CO) :
     StatusCO ="hazerd "
 elif( 15.5<=P_CO) :
     StatusCO ="very un halthey "
 elif ( 12.5<= P_CO<=15.4) :
     StatusCO ="un halthey "
 elif  ( 9.5<= P_CO<=12.4) :
     StatusCO ="unhealthy for sensitive group"
 elif  ( 4.9<= P_CO<=9.4) :
     StatusCO ="Modrate"
 elif  ( 0<= P_CO<=4.4) :
     StatusCO ="Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\CO"
 files=os.listdir(path)
 fpic=random.choice(files)
 COF= "CO/"+fpic
 NameCOPicF=fpic.split(".")[0]
 Image_FileCOF= url_for('static', filename=COF)      
 count=1
 noPic=3
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        COS= "CO/"+spic
        NameCOPicS=spic.split(".")[0]
        Image_FileCOS= url_for('static', filename=COS)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             COT= "CO/"+ tpic 
             NameCOPicT=tpic.split(".")[0]
             Image_FileCOT= url_for('static', filename=COT)
             count = count + 1
# --------------------------
# #   # END  Algorthim CO recomend 
# # -----------------------
 if (106<=P_O3) :
      statusO3 ="very un halthey "
 elif (86<= P_O3<=105) :
      statusO3= "unhealthy "
 elif (71<=P_O3<=85) :
      statusO3= "unhealthy for sensitive group"
 elif (55<= P_O3<=70) :
     statusO3= "Moudrate" 
 elif (0<= P_O3<=54) :
     statusO3= "Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\O3"
 files=os.listdir(path)
 fpic=random.choice(files)
 O3F= "O3/"+fpic
 NameO3PicF=fpic.split(".")[0]
 Image_FileO3F= url_for('static', filename=O3F)      
 count=1
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        O3S= "O3/"+spic
        NameO3PicS=spic.split(".")[0]
        Image_FileO3S= url_for('static', filename=O3S)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             O3T= "O3/"+ tpic 
             NameO3PicT=tpic.split(".")[0]
             Image_FileO3T= url_for('static', filename=O3T)
             count = count + 1
#Shrub
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\Shrub"
 files=os.listdir(path)
 fpic=random.choice(files)
 ShrubF= "Shrub/"+fpic
 NameShrubFPicF=fpic.split(".")[0]
 Image_FileShrubF= url_for('static', filename=ShrubF)      
 count=1
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        ShrubFS= "Shrub/"+spic
        NameShrubFSPicS=spic.split(".")[0]
        Image_FileShrubFSS= url_for('static', filename=ShrubFS)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             ShrubFST= "Shrub/"+ tpic 
             NameShrubFSTPicT=tpic.split(".")[0]
             Image_FileShrubFSTT= url_for('static', filename=ShrubFST)
             count = count + 1
 return render_template('RecomendTree.html',
                         n=n,Image_File=Image_File,NameFpic=NameFpic, m2=m2,Image_File1=Image_File1,NameSpic=NameSpic, m3=m3 ,Image_File11=Image_File11,NameTpic=NameTpic ,StatusPM25=StatusPM25,
                         NamePM10PicF=NamePM10PicF,Image_FilePM10F=Image_FilePM10F,NamePM10PicS=NamePM10PicS,Image_FilePM10S=Image_FilePM10S,NamePM10PicT=NamePM10PicT,Image_FilePM10T=Image_FilePM10T,StatusPM10=StatusPM10,
                         NameNOPicF=NameNOPicF,Image_FileNOF=Image_FileNOF,NameNOPicS=NameNOPicS,Image_FileNOS=Image_FileNOS,Image_FileNOT=Image_FileNOT,NameNOPicT=NameNOPicT,StatusNO=StatusNO,StatusCO=StatusCO,
                         NameCOPicF=NameCOPicF,Image_FileCOF=Image_FileCOF,NameCOPicS=NameCOPicS,Image_FileCOS=Image_FileCOS,Image_FileCOT=Image_FileCOT,NameCOPicT=NameCOPicT,
                         NameO3PicF=NameO3PicF,Image_FileO3F=Image_FileO3F,NameO3PicS=NameO3PicS,Image_FileO3S=Image_FileO3S,Image_FileO3T=Image_FileO3T,NameO3PicT=NameO3PicT, statusO3=statusO3,
                         NameShrubFPicF=NameShrubFPicF,Image_FileShrubF=Image_FileShrubF,NameShrubFSPicS=NameShrubFSPicS,Image_FileShrubFSS=Image_FileShrubFSS,NameShrubFSTPicT=NameShrubFSTPicT,Image_FileShrubFSTT=Image_FileShrubFSTT
                         )
 
@app.route("/Predict1", methods=["GET", "POST"])
def Predict1():
    P_PM25,P_PM10,P_NO2 ,P_CO,P_O3,P_AQI=Predict11()
    return render_template('Predict1.html', 
                           P_PM25 = P_PM25, P_PM10 = P_PM10, P_NO2 = P_NO2, P_CO = P_CO, P_O3 = P_O3, P_AQI = P_AQI)
     

@app.route("/RecomendTree1" ,methods=["GET", "POST"])
def RecomendTree1(): 
 P_PM25,P_PM10,P_NO2 ,P_CO,P_O3,P_AQI=SENDP1()
 # Algorthim PM2.5 recomend 
 if (250.5 <=P_PM25) :
      StatusPM25='hazerd'
 elif(105.5<= P_PM25<=250.4) :
      StatusPM25 ="very unhalthey "
 elif ( 55.5<=P_PM25<=150.4) :
      StatusPM25= "unhealthy "          
 elif (35.5<= P_PM25<=55.4) :
      StatusPM25= "unhealthy for sensitive group"  
 elif (12.1<= P_PM25<=35.4) :
      StatusPM25= "Moudrate" 
 elif (0<= P_PM25<=12) :
      StatusPM25= "Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\PM2.5"
 files=os.listdir(path)
 fpic=random.choice(files)
 n= "PM2.5/"+fpic
 NameFpic=fpic.split(".")[0]
 Image_File= url_for('static', filename=n)      
 count=1
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        m2= "PM2.5/"+spic
        NameSpic=spic.split(".")[0]
        Image_File1= url_for('static', filename=m2)
        count = count + 1
        # if count==noPic:
        #     break
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             m3= "PM2.5/"+ tpic 
             NameTpic=tpic.split(".")[0]
             Image_File11= url_for('static', filename=m3)
             count = count + 1
#    End  Algorthim PM2.5 recomend 
# -----------------------------------------------------------------------------
  # Algorthim PM10 recomend 
 if ( 425<= P_PM10) :
      StatusPM10="hazerd"
 elif( 355<= P_PM10<=424) :
       StatusPM10 ="very unhalthey "
 elif( 255<= P_PM10<=354) :
       StatusPM10= "unhealthy "
 elif ( 155<= P_PM10<=254) :
       StatusPM10= "unhealthy for sensitive group"
 elif  ( 55<= P_PM10<=154) :
      StatusPM10 ="Modrate"
 elif  ( 0<= P_PM10<=54) :
      StatusPM10="Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\PM10"
 files=os.listdir(path)
 fpic=random.choice(files)
 PMF= "PM10/"+fpic
 NamePM10PicF=fpic.split(".")[0]
 Image_FilePM10F= url_for('static', filename=PMF)      
 count=1
 noPic=3
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        PMS= "PM10/"+spic
        NamePM10PicS=spic.split(".")[0]
        Image_FilePM10S= url_for('static', filename=PMS)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             PMT= "PM10/"+ tpic 
             NamePM10PicT=tpic.split(".")[0]
             Image_FilePM10T= url_for('static', filename=PMT)
             count = count + 1
  #  End Algorthim PM10 recomend 
# # ---------------------------------
# #    # Algorthim NO2 recomend 
 if ( 1250<= P_NO2) :
     StatusNO ="hazerd "
 elif( 650<= P_NO2<=1249) :
     StatusNO ="very un halthey "
 elif ( 361<= P_NO2<=649) :
     StatusNO= "unhealthy "
 elif (101<= P_NO2<=360) :
     StatusNO= "unhealthy for sensitive group"    
 elif (54<= P_NO2<=100) :
      StatusNO= "Moudrate"
 elif (0<= P_NO2<=53) :
     StatusNO= "Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\NO2"
 files=os.listdir(path)
 fpic=random.choice(files)
 NOF= "NO2/"+fpic
 NameNOPicF=fpic.split(".")[0]
 Image_FileNOF= url_for('static', filename=NOF)      
 count=1
 noPic=3
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        NOS= "NO2/"+spic
        NameNOPicS=spic.split(".")[0]
        Image_FileNOS= url_for('static', filename=NOS)
        count = count + 1
        if count==noPic:
            break
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             NOT= "NO2/"+ tpic 
             NameNOPicT=tpic.split(".")[0]
             Image_FileNOT= url_for('static', filename=NOT)
             count = count + 1
#   #  END Algorthim NO2 recomend
# --------------------------
# #    # Algorthim CO recomend 
 if ( 30.5<=P_CO) :
     StatusCO ="hazerd "
 elif( 15.5<=P_CO<=30.4) :
     StatusCO ="very un halthey "
 elif ( 12.5<= P_CO<=15.4) :
     StatusCO ="un halthey "
 elif  ( 9.5<= P_CO<=12.4) :
     StatusCO ="unhealthy for sensitive group"
 elif  ( 4.9<= P_CO<=9.4) :
     StatusCO ="Modrate"
 elif  ( 0<= P_CO<=4.4) :
     StatusCO ="Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\CO"
 files=os.listdir(path)
 fpic=random.choice(files)
 COF= "CO/"+fpic
 NameCOPicF=fpic.split(".")[0]
 Image_FileCOF= url_for('static', filename=COF)      
 count=1
 noPic=3
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        COS= "CO/"+spic
        NameCOPicS=spic.split(".")[0]
        Image_FileCOS= url_for('static', filename=COS)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             COT= "CO/"+ tpic 
             NameCOPicT=tpic.split(".")[0]
             Image_FileCOT= url_for('static', filename=COT)
             count = count + 1
# --------------------------
# #   # END  Algorthim CO recomend 
# # -----------------------
 if (106<=P_O3) :
      statusO3 ="very un halthey "
 elif (86<= P_O3<=105) :
      statusO3= "unhealthy "
 elif (71<=P_O3<=85) :
      statusO3= "unhealthy for sensitive group"
 elif (55<= P_O3<=70) :
     statusO3= "Moudrate" 
 elif (0<= P_O3<=54) :
     statusO3= "Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\O3"
 files=os.listdir(path)
 fpic=random.choice(files)
 O3F= "O3/"+fpic
 NameO3PicF=fpic.split(".")[0]
 Image_FileO3F= url_for('static', filename=O3F)      
 count=1
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        O3S= "O3/"+spic
        NameO3PicS=spic.split(".")[0]
        Image_FileO3S= url_for('static', filename=O3S)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             O3T= "O3/"+ tpic 
             NameO3PicT=tpic.split(".")[0]
             Image_FileO3T= url_for('static', filename=O3T)
             count = count + 1
#Shrub
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\Shrub"
 files=os.listdir(path)
 fpic=random.choice(files)
 ShrubF= "Shrub/"+fpic
 NameShrubFPicF=fpic.split(".")[0]
 Image_FileShrubF= url_for('static', filename=ShrubF)      
 count=1
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        ShrubFS= "Shrub/"+spic
        NameShrubFSPicS=spic.split(".")[0]
        Image_FileShrubFSS= url_for('static', filename=ShrubFS)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             ShrubFST= "Shrub/"+ tpic 
             NameShrubFSTPicT=tpic.split(".")[0]
             Image_FileShrubFSTT= url_for('static', filename=ShrubFST)
             count = count + 1
 return render_template('RecomendTree.html',
                         n=n,Image_File=Image_File,NameFpic=NameFpic, m2=m2,Image_File1=Image_File1,NameSpic=NameSpic, m3=m3 ,Image_File11=Image_File11,NameTpic=NameTpic ,StatusPM25=StatusPM25,
                         NamePM10PicF=NamePM10PicF,Image_FilePM10F=Image_FilePM10F,NamePM10PicS=NamePM10PicS,Image_FilePM10S=Image_FilePM10S,NamePM10PicT=NamePM10PicT,Image_FilePM10T=Image_FilePM10T,StatusPM10=StatusPM10,
                         NameNOPicF=NameNOPicF,Image_FileNOF=Image_FileNOF,NameNOPicS=NameNOPicS,Image_FileNOS=Image_FileNOS,Image_FileNOT=Image_FileNOT,NameNOPicT=NameNOPicT,StatusNO=StatusNO,StatusCO=StatusCO,
                         NameCOPicF=NameCOPicF,Image_FileCOF=Image_FileCOF,NameCOPicS=NameCOPicS,Image_FileCOS=Image_FileCOS,Image_FileCOT=Image_FileCOT,NameCOPicT=NameCOPicT,
                         NameO3PicF=NameO3PicF,Image_FileO3F=Image_FileO3F,NameO3PicS=NameO3PicS,Image_FileO3S=Image_FileO3S,Image_FileO3T=Image_FileO3T,NameO3PicT=NameO3PicT, statusO3=statusO3,
                         NameShrubFPicF=NameShrubFPicF,Image_FileShrubF=Image_FileShrubF,NameShrubFSPicS=NameShrubFSPicS,Image_FileShrubFSS=Image_FileShrubFSS,NameShrubFSTPicT=NameShrubFSTPicT,Image_FileShrubFSTT=Image_FileShrubFSTT
                         )

@app.route("/Predict2", methods=["GET", "POST"])
def Predict2():
    P_PM25,P_PM10,P_NO2 ,P_CO,P_O3,P_AQI=Predict211()
    return render_template('Predict2.html', 
                           P_PM25 = P_PM25, P_PM10 = P_PM10, P_NO2 = P_NO2, P_CO = P_CO, P_O3 = P_O3, P_AQI = P_AQI)
     

@app.route("/RecomendTree2" ,methods=["GET", "POST"])
def RecomendTree2(): 
 P_PM25,P_PM10,P_NO2 ,P_CO,P_O3,P_AQI=SENDP111()
 # Algorthim PM2.5 recomend 
 if (250.5 <=P_PM25) :
      StatusPM25='hazerd'
 elif(105.5<= P_PM25<=250.4) :
      StatusPM25 ="very unhalthey "
 elif ( 55.5<=P_PM25<=150.4) :
      StatusPM25= "unhealthy "          
 elif (35.5<= P_PM25<=55.4) :
      StatusPM25= "unhealthy for sensitive group"  
 elif (12.1<= P_PM25<=35.4) :
      StatusPM25= "Moudrate" 
 elif (0<= P_PM25<=12) :
      StatusPM25= "Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\PM2.5"
 files=os.listdir(path)
 fpic=random.choice(files)
 n= "PM2.5/"+fpic
 NameFpic=fpic.split(".")[0]
 Image_File= url_for('static', filename=n)      
 count=1
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        m2= "PM2.5/"+spic
        NameSpic=spic.split(".")[0]
        Image_File1= url_for('static', filename=m2)
        count = count + 1
        # if count==noPic:
        #     break
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             m3= "PM2.5/"+ tpic 
             NameTpic=tpic.split(".")[0]
             Image_File11= url_for('static', filename=m3)
             count = count + 1
#    End  Algorthim PM2.5 recomend 
# -----------------------------------------------------------------------------
  # Algorthim PM10 recomend 
 if ( 425<= P_PM10) :
      StatusPM10="hazerd"
 elif( 355<= P_PM10<=424) :
       StatusPM10 ="very unhalthey "
 elif( 255<= P_PM10<=354) :
       StatusPM10= "unhealthy "
 elif ( 155<= P_PM10<=254) :
       StatusPM10= "unhealthy for sensitive group"
 elif  ( 55<= P_PM10<=154) :
      StatusPM10 ="Modrate"
 elif  ( 0<= P_PM10<=54) :
      StatusPM10="Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\PM10"
 files=os.listdir(path)
 fpic=random.choice(files)
 PMF= "PM10/"+fpic
 NamePM10PicF=fpic.split(".")[0]
 Image_FilePM10F= url_for('static', filename=PMF)      
 count=1
 noPic=3
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        PMS= "PM10/"+spic
        NamePM10PicS=spic.split(".")[0]
        Image_FilePM10S= url_for('static', filename=PMS)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             PMT= "PM10/"+ tpic 
             NamePM10PicT=tpic.split(".")[0]
             Image_FilePM10T= url_for('static', filename=PMT)
             count = count + 1
  #  End Algorthim PM10 recomend 
# # ---------------------------------
# #    # Algorthim NO2 recomend 
 if ( 1250<= P_NO2) :
     StatusNO ="hazerd "
 elif( 650<= P_NO2<=1249) :
     StatusNO ="very un halthey "
 elif ( 361<= P_NO2<=649) :
     StatusNO= "unhealthy "
 elif (101<= P_NO2<=360) :
     StatusNO= "unhealthy for sensitive group"    
 elif (54<= P_NO2<=100) :
      StatusNO= "Moudrate"
 elif (0<= P_NO2<=53) :
     StatusNO= "Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\NO2"
 files=os.listdir(path)
 fpic=random.choice(files)
 NOF= "NO2/"+fpic
 NameNOPicF=fpic.split(".")[0]
 Image_FileNOF= url_for('static', filename=NOF)      
 count=1
 noPic=3
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        NOS= "NO2/"+spic
        NameNOPicS=spic.split(".")[0]
        Image_FileNOS= url_for('static', filename=NOS)
        count = count + 1
        if count==noPic:
            break
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             NOT= "NO2/"+ tpic 
             NameNOPicT=tpic.split(".")[0]
             Image_FileNOT= url_for('static', filename=NOT)
             count = count + 1
#   #  END Algorthim NO2 recomend
# --------------------------
# #    # Algorthim CO recomend 
 if ( 30.5<=P_CO) :
     StatusCO ="hazerd "
 elif( 15.5<=P_CO<=30.4) :
     StatusCO ="very un halthey "
 elif ( 12.5<= P_CO<=15.4) :
     StatusCO ="un halthey "
 elif  ( 9.5<= P_CO<=12.4) :
     StatusCO ="unhealthy for sensitive group"
 elif  ( 4.9<= P_CO<=9.4) :
     StatusCO ="Modrate"
 elif  ( 0<= P_CO<=4.4) :
     StatusCO ="Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\CO"
 files=os.listdir(path)
 fpic=random.choice(files)
 COF= "CO/"+fpic
 NameCOPicF=fpic.split(".")[0]
 Image_FileCOF= url_for('static', filename=COF)      
 count=1
 noPic=3
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        COS= "CO/"+spic
        NameCOPicS=spic.split(".")[0]
        Image_FileCOS= url_for('static', filename=COS)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             COT= "CO/"+ tpic 
             NameCOPicT=tpic.split(".")[0]
             Image_FileCOT= url_for('static', filename=COT)
             count = count + 1
# --------------------------
# #   # END  Algorthim CO recomend 
# # -----------------------
 if (106<=P_O3) :
      statusO3 ="very un halthey "
 elif (86<= P_O3<=105) :
      statusO3= "unhealthy "
 elif (71<=P_O3<=85) :
      statusO3= "unhealthy for sensitive group"
 elif (55<= P_O3<=70) :
     statusO3= "Moudrate" 
 elif (0<= P_O3<=54) :
     statusO3= "Good"
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\O3"
 files=os.listdir(path)
 fpic=random.choice(files)
 O3F= "O3/"+fpic
 NameO3PicF=fpic.split(".")[0]
 Image_FileO3F= url_for('static', filename=O3F)      
 count=1
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        O3S= "O3/"+spic
        NameO3PicS=spic.split(".")[0]
        Image_FileO3S= url_for('static', filename=O3S)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             O3T= "O3/"+ tpic 
             NameO3PicT=tpic.split(".")[0]
             Image_FileO3T= url_for('static', filename=O3T)
             count = count + 1
#Shrub
 path="C:\\Users\\hp\\Desktop\\GPF\\static\\Shrub"
 files=os.listdir(path)
 fpic=random.choice(files)
 ShrubF= "Shrub/"+fpic
 NameShrubFPicF=fpic.split(".")[0]
 Image_FileShrubF= url_for('static', filename=ShrubF)      
 count=1
 while (count<2):
     spic=random.choice(files)
     if (spic!=fpic):
        ShrubFS= "Shrub/"+spic
        NameShrubFSPicS=spic.split(".")[0]
        Image_FileShrubFSS= url_for('static', filename=ShrubFS)
        count = count + 1
 while (count<3):
        tpic=random.choice(files)
        if(tpic!=fpic)and(tpic!=spic):
             ShrubFST= "Shrub/"+ tpic 
             NameShrubFSTPicT=tpic.split(".")[0]
             Image_FileShrubFSTT= url_for('static', filename=ShrubFST)
             count = count + 1
 return render_template('RecomendTree2.html',
                         n=n,Image_File=Image_File,NameFpic=NameFpic, m2=m2,Image_File1=Image_File1,NameSpic=NameSpic, m3=m3 ,Image_File11=Image_File11,NameTpic=NameTpic ,StatusPM25=StatusPM25,
                         NamePM10PicF=NamePM10PicF,Image_FilePM10F=Image_FilePM10F,NamePM10PicS=NamePM10PicS,Image_FilePM10S=Image_FilePM10S,NamePM10PicT=NamePM10PicT,Image_FilePM10T=Image_FilePM10T,StatusPM10=StatusPM10,
                         NameNOPicF=NameNOPicF,Image_FileNOF=Image_FileNOF,NameNOPicS=NameNOPicS,Image_FileNOS=Image_FileNOS,Image_FileNOT=Image_FileNOT,NameNOPicT=NameNOPicT,StatusNO=StatusNO,StatusCO=StatusCO,
                         NameCOPicF=NameCOPicF,Image_FileCOF=Image_FileCOF,NameCOPicS=NameCOPicS,Image_FileCOS=Image_FileCOS,Image_FileCOT=Image_FileCOT,NameCOPicT=NameCOPicT,
                         NameO3PicF=NameO3PicF,Image_FileO3F=Image_FileO3F,NameO3PicS=NameO3PicS,Image_FileO3S=Image_FileO3S,Image_FileO3T=Image_FileO3T,NameO3PicT=NameO3PicT, statusO3=statusO3,
                         NameShrubFPicF=NameShrubFPicF,Image_FileShrubF=Image_FileShrubF,NameShrubFSPicS=NameShrubFSPicS,Image_FileShrubFSS=Image_FileShrubFSS,NameShrubFSTPicT=NameShrubFSTPicT,Image_FileShrubFSTT=Image_FileShrubFSTT
                         )



if __name__ == "__main__":
   app.run(debug=True, port=900) 


