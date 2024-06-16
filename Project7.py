## Predicting Singapore Resale Flat Prices


#import usefull libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")
import streamlit as st    
import pickle
from sklearn.ensemble import RandomForestRegressor


#To set Background fo streamlit app
st.set_page_config(layout='wide')
st.title(":rainbow[ Singapore  Resale Flat Prices Predicting]")
tab1,tab2=st.tabs(["HOME","APPLICATION (PREDICT Resale Flat Prices )"])
with tab1:
    st.text_area(":green[ABOUT PROJECT]:","The resale flat market in Singapore is highly competitive, and it can be challenging to accurately estimate the resale value of a flat. There are many factors that can affect resale prices, such as location, flat type, floor area, and lease duration. A predictive model can help to overcome these challenges by providing users with an estimated resale price based on these factors ")

    st.text_area(":green[Tools Used For this Project]","Python,VSCODE ,Streamlit")

    st.text_area(":green[Project created by]","ARSHINA.P,     contact:arshizig7@gmail.com")

#To access user inputs
with tab2:
    town=st.sidebar.selectbox(":red[Select Town] ",('ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
       'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
       'GEYLANG', 'HOUGANG', 'JURONG', 'JURONG WEST',
       'KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG',
       'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN',
       'LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS',
       'PUNGGOL'))
    
    if town=='ANG MO KIO':
        town=0
    elif town=='BEDOK':
        town=1
    elif town=='BISHAN':
        town=2
    elif town=='BUKIT BATOK':
        town=3
    elif town=='BUKIT MERAH':
        town=4
    elif town=='BUKIT TIMAH':
        town=6
    elif town=='CENTRAL AREA':
        town=7
    elif town=='CHOA CHU KANG':
        town=8
    elif town=='CLEMENTI':
        town=9
    elif town=='GEYLANG':
        town=10
    elif town=='HOUGANG':
        town=11
    elif town=='JURONG':
        town=12
    elif town=='JURONG WEST':
        town=13
    elif town=='KALLANG/WHAMPOA':
        town=14
    elif town=='MARINE PARADE':
        town=16
    elif town=='QUEENSTOWN':
        town=19
    elif town=='SENGKANG':
        town=21
    elif town=='SERANGOON':
        town=22
    elif town=='TAMPINES':
        town=23
    elif town=='TOA PAYOH':
        town=24
    elif town=='WOODLANDS':
        town=25
    elif town=='YISHUN':
        town=26
    elif town=='LIM CHU KANG':
        town=15
    elif town=='SEMBAWANG':
        town=20
    elif town=='BUKIT PANJANG':
        town=5
    elif town=='PASIR RIS':
        town=17
    elif town=='PUNGGOL':
        town=18


    flat_type=st.sidebar.selectbox(":red[Select Flat Type]",('1 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE','MULTI GENERATION', 'MULTI-GENERATION'))
    if flat_type=="1 ROOM":
        flat_type=0
    elif flat_type=="3 ROOM":
         flat_type=2
    elif flat_type=="4 ROOM":
         flat_type=3
    elif flat_type=="5 ROOM":
         flat_type=4
    elif flat_type=="2 ROOM":
         flat_type=1
    elif flat_type=="EXECUTIVE":
         flat_type=5
    elif flat_type=="MULTI GENERATION":
         flat_type=6
    elif flat_type=="MULTI-GENERATION":
         flat_type=7


    flat_model=st.sidebar.selectbox(":red[Select Flat Model]",('IMPROVED', 'NEW GENERATION', 'MODEL A', 'STANDARD', 'SIMPLIFIED',
       'MODEL A-MAISONETTE', 'APARTMENT', 'MAISONETTE', 'TERRACE',
       '2-ROOM', 'IMPROVED-MAISONETTE', 'MULTI GENERATION',
       'PREMIUM APARTMENT', 'Improved', 'New Generation', 'Model A',
       'Standard', 'Apartment', 'Simplified', 'Model A-Maisonette',
       'Maisonette', 'Multi Generation', 'Adjoined flat',
       'Premium Apartment', 'Terrace', 'Improved-Maisonette',
       'Premium Maisonette', '2-room', 'Model A2', 'DBSS', 'Type S1',
       'Type S2', 'Premium Apartment Loft', '3Gen'))
    if flat_model=="IMPROVED":
        flat_model=7
    elif flat_model=="NEW GENERATION":
        flat_model=20
    elif flat_model=="MODEL A":
        flat_model=12
    elif flat_model=="STANDARD":
        flat_model=27
    elif flat_model=="SIMPLIFIED":
        flat_model=26
    elif flat_model=="MODEL A-MAISONETTE":
        flat_model=13
    elif flat_model=="APARTMENT":
        flat_model=3
    elif flat_model=="MAISONETTE":
        flat_model=11
    elif flat_model=="TERRACE":
        flat_model=30
    elif flat_model=="2-ROOM":
        flat_model=0
    elif flat_model=="IMPROVED-MAISONETTE":
        flat_model=8
    elif flat_model=="MULTI GENERATION":
        flat_model=14
    elif flat_model=="PREMIUM APARTMENT":
        flat_model=22
    elif flat_model=="Improved":   
        flat_model=9
    elif flat_model=="New Generation":
        flat_model=21
    elif flat_model=="Model A":
        flat_model=16
    elif flat_model=="Standard":
        flat_model=29
    elif flat_model=="Apartment":
        flat_model=5
    elif flat_model=="Simplified":
        flat_model=28
    elif flat_model=="Model A-Maisonette":
        flat_model=17
    elif flat_model=="Maisonette":                                 
        flat_model=15
    elif flat_model=="Multi Generation":
        flat_model=19
    elif flat_model=="Adjoined flat":
        flat_model=4
    elif flat_model=="Premium Apartment":
        flat_model=23
    elif flat_model=="Terrace":
        flat_model=31
    elif flat_model=="Improved-Maisonette":
        flat_model=10
    elif flat_model=="Premium Maisonette":
        flat_model=25
    elif flat_model=="2-room":
        flat_model=1
    elif flat_model=="Model A2":
        flat_model=18
    elif flat_model=="DBSS":
        flat_model=6
    elif flat_model=="Type S1":
        flat_model=32
    elif flat_model=="Type S2":
        flat_model=33
    elif flat_model=="Premium Apartment Loft":
        flat_model=24
    elif flat_model=="3Gen":
        flat_model=2
        
    lease_commence_date=st.sidebar.selectbox(":red[Select Flat Model]",('1977', '1976', '1978', '1979', '1984', '1980', '1985', '1981', '1982', '1986', '1972',
       '1983', '1973', '1969', '1975', '1971', '1974', '1967', '1970', '1968', '1988', '1987',
       '1989', '1990', '1992', '1993', '1994', '1991', '1995', '1996', '1997', '1998', '1999',
       '2000', '2001', '1966', '2002', '2006', '2003', '2005', '2004', '2008', '2007', '2009',
       '2010', '2012', '2011', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2022',
       '2020'))
    lease_commence_date=np.log(int(lease_commence_date))
    


    year=st.sidebar.selectbox(":red[Select Year]",('1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000',
       '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022',
       '2023', '2024'))
    year=int(year)
    remaining_lease_year=st.sidebar.selectbox(":red[Select Remaining_lease_year]",('0', '70', '65', '64', '63', '62', '69', '60', '61', '86', '77', '80', '90', '87', '66', '58', '94',
       '71', '68', '84', '73', '79', '76', '72', '82', '74', '67', '88', '81', '89', '53', '54', '55', '57',
       '93', '83', '85', '92', '91', '59', '95', '52', '51', '56', '75', '96', '78', '50', '97', '49', '48',
       '47', '46', '45', '44', '43', '42', '41'))
    
    remaining_lease_year=np.cbrt(int(remaining_lease_year))



    remaining_lease_month=st.sidebar.selectbox(":red[Select Remaining_lease_month]",('0' , '1' , '2'  ,'3' , '4' , '5',  '6' , '7' , '8' , '9', '10' ,'11'))
    remaining_lease_month=np.cbrt(int(remaining_lease_month))
    
    
    
    storey_start=st.sidebar.selectbox(":red[Select Storey_start]",('10',  '4',  '7',  '1', '13', '19', '16',  '6', '11'))
    storey_start=np.log(int(storey_start))

    storey_end=st.sidebar.selectbox(":red[Select Storey_end]",( '0',  '1',  '2',  '3',  '4',  '6',  '7',  '8',  '9', '10', '11', '12', '13', '14', '16', '19', '21',
       '22', '23', '24', '25', '26', '15', '20',  '5', '17', '18'))
    storey_end=np.log(int(storey_end))

    floor_area_sqm=st.sidebar.number_input(":red[Enter the Value of Floor Area sqm (Min: 28 / Max: 307)]")
    floor_area_sqm=float(floor_area_sqm)

    data={"town":town,"flat_type":flat_type,"floor_area_sqm":floor_area_sqm,"flat_model":flat_model,"year":year,"remaining_lease_year_cbrt":remaining_lease_year,"remaining_lease_month_cbrt":remaining_lease_month,"lease_commence_date_log":lease_commence_date,"storey_start_log":storey_start,"storey_end_log":storey_end}
    dataframe=pd.DataFrame(data,index=[1])
    
    with open("Regressor_Resale.pk1","rb") as f:                        
       model_=pickle.load(f)

    with open("standerd_scalar.pk1","rb") as f1:
        Sc=pickle.load(f1)

    

    #To predict resale prices
    scale_data=Sc.transform(dataframe)
    prediction=model_.predict(scale_data)
    
    st.write("select the requirment from the sidebar")
    result=st.button("Click here to predict Resale flat price")
    if result:
           st.write(prediction)

#Here completed the Project ## Predicting Singapore Resale Flat Prices##

                 