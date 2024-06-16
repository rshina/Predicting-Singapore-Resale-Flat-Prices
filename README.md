# Predicting-Singapore-Resale-Flat-Prices

## Problem Statement:


       The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. This predictive model will be based on historical data of resale flat transactions, and it aims to assist both potential buyers and sellers in estimating the resale value of a flat.

## Regression model :


             The resale flat market in Singapore is highly competitive, and it can be challenging to accurately estimate the resale value of a flat. There are many factors that can affect resale prices, such as location, flat type, floor area, and lease duration. A predictive model can help to overcome these challenges by providing users with an estimated resale price based on these factors.


## Work Flow:


      * Import necessery libraries
      * Load the data
      * EDA process to know the information about the data
      * Preprocessing:


                  **Handling missing values
                  **Handling the data which are in wrong format
                  **Ckeck the distribution of the data and remove the skewness if its skewed
                  **Handling outliers
                  **Check the correlation of features using heat map

                  
       * Split the features as test and train for ML precessing
       * Select the  Machine Learning  model which should give better perfomance than others
       * Train the model using selected algorithm
       * Evaluation of selected model
       *  Store the model using pickling method(serialising),and can De serialise or load the data when it utalize anywhere

       * Streamlit App
                Take the predictive power live on Streamlit Cloud:
                In the Streamlit app, we are getting the inputs from the user to make the prediction and running the app to display the predicted resale price value. 

       
Here completed the project Industrial-Copper-Modeling

created by ARSHINA.P arshizig7@gmail.com
