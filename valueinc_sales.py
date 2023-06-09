# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 23:12:07 2023

@author: hp
"""

import pandas as pd

#To read csv file we use read.csv function
# data = pd.read.csv('file.csv') <--- format of read.csv
data = pd.read_csv('transaction2.csv',sep = ';')

#summary of the data
data.info()

#extra calculations
CostPerItem = 14.6
SellingPricePerItem = 16
NumberOfItemsPurchased = 7

ProfitPerItem = 16-14.6
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem 
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#Now doing calculation in real dataset
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

SellingPricePerItem = data['SellingPricePerItem']
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#Now saving it
data['CostPerTransaction'] = CostPerTransaction
data['SellingPricePerTransaction'] = SellingPricePerTransaction

data['ProfitPerTransaction'] = data['SellingPricePerTransaction'] - data['CostPerTransaction']

data['Markup'] = (data['SellingPricePerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

#Rounding elements to 2 decimal places
roundMarkup = round(data['Markup'],2)

data['Markup']= roundMarkup

#combining data fields
#mydate = data['Day'] + '-'

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)

mydate = day + '-' + data['Month'] + '-' + year

data['date'] = mydate

#using iloc to view rows and columns
data.iloc[0]     #first row
data.iloc[0:3]   #first 3 rows
data.iloc[-5:]   #last 3 rows

data.head()      #also shows first 5 rows

data.iloc[:,2]   #shows all rows on a specific column

data.iloc[4,2]   #shows 4 row on the 2 column

#using functions to clean the data
#split function

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns from that
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#now replacing square brackets from clientage and lengthofcharacter
data['ClientAge'] = data['ClientAge'].str.replace("[","")
data['LengthOfContract'] = data['LengthOfContract'].str.replace("]","")

#using lower function
data['ItemDescription'] = data['ItemDescription'].str.lower()

#bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#now merging both datasets
data = pd.merge(data,seasons , on='Month')

#dropping useless columns 
data = data.drop('ClientKeywords', axis=1)
data = data.drop('Day', axis=1)
data = data.drop('Month', axis=1)
data = data.drop('Year', axis=1)

#exporting to csv file
data.to_csv('ValueIncCleaned.csv', index=False)