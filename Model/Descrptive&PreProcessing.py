#import libraries
import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split,GridSearchCV,learning_curve
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score

def linear_scale(col):
    xmin = float(col.min())
    xmax = float(col.max())
    return col.apply(lambda x: (x-xmin)/(xmax-xmin))

margin = '___________+++++____________________++++++_____________________+++++________'
asking = ['press y then Enter To View ',' else press any key: ']
# load the dataset
df = pd.read_csv('train.csv')

# change the parameter of number of columns to show in cmd
pd.set_option('display.max_columns',15)

inp = input(asking[0]+'DataSet'+asking[1])
print(margin)
if inp == 'y':
    print('\n')
    print(df.head())
    print(margin)
inp = input(asking[0]+'infomation'+asking[1])
print(margin)
if(inp == 'y'):
    print('\n')
    # information about the dataset
    print(df.info())
    print(margin)
inp = input(asking[0]+'Report of missing values'+asking[1])
print(margin)
if inp == 'y':
    print('\n')
    # which columns is missing values
    print("Which columns contain null values")
    print(df.isnull().any())
    #compute the count of missing values
    print("Total number of items with missing values")
    print(df.isnull().sum())
    #compute the percentage of the missing values
    print("Percentage of the missing values per column")
    missing_value = (df.isnull().sum()/df.shape[0]*100)
    # removing 0 percent form the missing_value
    missing_value = missing_value[missing_value != 0].round(2)
    print(missing_value)
    print(margin)
#Preprocessing
#missing values in product categoriy 2,product categroy 3
#filling  the missing Values
df.Product_Category_2.fillna(df.Product_Category_2.mode()[0],inplace=True)
df.Product_Category_3.fillna(df.Product_Category_3.mode()[0],inplace=True)
LE = LabelEncoder()
X = df.drop(["Purchase"],axis=1)
X = X.apply(LE.fit_transform)
columns_names = X.columns.values

Y = df['Purchase']
Y = Y.to_frame()
SS = StandardScaler()
Xs_array = SS.fit_transform(X.astype('float'))

Xs = pd.DataFrame({columns_names[i]:Xs_array[:,i] for i in range(len(columns_names))})
Xl = X.copy()
Xl.Product_ID = linear_scale(Xl.Product_ID)
Xl.Age = linear_scale(Xl.Age)
Xl.Occupation = linear_scale(Xl.Occupation)
Xl.Stay_In_Current_City_Years = linear_scale(Xl.Stay_In_Current_City_Years)
Xl.City_Category = linear_scale(Xl.City_Category)
Xl.Product_Category_1 = linear_scale(Xl.Product_Category_1)
Xl.Product_Category_2 = linear_scale(Xl.Product_Category_2)
Xl.Product_Category_3 = linear_scale(Xl.Product_Category_3)
inp = input(asking[0]+"DataSet After Preprocessing"+asking[1])
print(margin)
if inp == 'y':
    print("Original DataFrame")
    print(X.head())
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Linear Scale DataFrame")
    print(Xl.head())
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Standard Scale DataFrame")
    print(Xs.head())
    print(margin)
inp = input(asking[0]+'Data information after Preprocessing'+asking[1])
print(margin)
if inp == 'y':
    print('\n')
    print(df.info())
    print(margin)

# put unique count of every column in dictionary
unique_count = {}
for col in df.columns:
    unique_count[col] = df[col].nunique()

inp = input(asking[0]+'number of unique item every column'+asking[1])
print(margin)
if inp == 'y':
    print('\n')
    # count of the unique elements in each column
    print("Total number of Rows : ",df.shape[0])
    for key,value in unique_count.items():
        print(str(key)+' unique elements : '+str(value))
    print(margin)

inp = input(asking[0]+'General Descriptive Information'+asking[1])
print(margin)
if inp == 'y':
    print('\n')
    print('The average number of items Purchased per customer = {} item'.format(int(df.shape[0]/unique_count['User_ID'])))
    print('The most Product_ID has been bought = ',df['Product_ID'].mode()[0])
    print('Total Purchase for the last month = {}$'.format(df.Purchase.sum()))
    print('The avergae Purchase price per person = {}$'.format(df.Purchase.sum()/unique_count['User_ID']))
    print(margin)

# compute new DataFrame Purchase per user
unique_userID = list(set(df.User_ID))
total_purchase = []
for UID in unique_userID:
    total_purchase.append(df[df['User_ID'] == UID]['Purchase'].sum())
df_User_totalPurchase = pd.DataFrame({'User_ID':unique_userID,'Total_Purchase':total_purchase})
inp = input(asking[0]+'DataFrame Total Purchase Per User'+asking[1])
print(margin)
if inp == 'y':
    print('\n')
    print(df_User_totalPurchase.head(10))
    print(margin)

max_Purchase = df_User_totalPurchase.Total_Purchase.max()
max_customerID = df_User_totalPurchase[df_User_totalPurchase['Total_Purchase']==df_User_totalPurchase.Total_Purchase.max()]['User_ID'].values[0]

inp = input(asking[0]+'Information About Unique Users DataSet'+asking[1])
if inp == 'y':
    print('The most Purchase has been bought by customer : {}$'.format(max_Purchase))
    print('The customer ID with most Purchase in the last month : ',max_customerID)
    print('The city Category for the most Purchase : ',df[df['User_ID']==max_customerID]['City_Category'].unique()[0])

print("*************************Done Descriptive*************************")
print("Saving the DataSets")
X.to_csv("X_train.csv",index=False)
Xl.to_csv("X_train_LinearScaleDF.csv",index=False)
Xs.to_csv("X_train_StandardScaleDF.csv",index=False)
Y.to_csv("Y_train.csv",index=False)
df_User_totalPurchase.to_csv("unique_userID.csv",index=False)
print("DataSet Saved")
print("BYE")
