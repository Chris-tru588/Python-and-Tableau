# -*- coding: utf-8 -*-
"""
Created on Sat May 13 13:51:26 2023

@author: chris
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

# summary of the data
data.info()

# working with calculation

# defining variables

costPerItem = 11.73
sellingPricePerItem = 21.11
numberOfItemsPerchased = 6

#mathematical operations on tableau

profitPerItem = sellingPricePerItem - costPerItem 

profitPerTransaction = numberOfItemsPerchased * profitPerItem

costPerTransaction = costPerItem * numberOfItemsPerchased
sellingPricePerTransaction = sellingPricePerItem * numberOfItemsPerchased


# costPerTransaction collumn calculation
#costPerTransaction = costPerItem * numberOfItemsPerchased
# Variable = dataframe['collumn name']

costPerItem = data['CostPerItem']
numberOfItemsPerchased = data['NumberOfItemsPurchased']
costPerTransaction = costPerItem * numberOfItemsPerchased

#adding new collumn to dataframe

data['costPerTransaction'] = costPerTransaction


#salesPerTransaction
data['salesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calculation = sales - cost

data['profitPerTransaction'] = data['salesPerTransaction'] - data['costPerTransaction']

#markup = (sales - cost)/cost

data['markUp'] = (data['profitPerTransaction'])/data['costPerTransaction']


#Rounding markUp

roundMarkUp = round(data['markUp'], 2)

data['markUp'] = round(data['markUp'], 2)


#combining data fields

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#my_date = data['Day'+]

#checking column datatype

print(data['Day'].dtype)


#change column type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-' + year

data['date'] = my_date

#using iloc to view specific columns/rows

data.iloc[0] #views the row with index = 0

data.iloc[0:3] #first 3 rows

data.iloc[-5:] #last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows on the second column

data.iloc[4,2] #brings in 4th row 2nd column


#using split to split the client keywords field
#new_var = column.str.split('sep', expand = True)


split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new column for the split column in client keyword
data['clientAge'] = split_col[0]
data['clientType'] = split_col[1]
data['lengthOfContract'] = split_col[2]

#using the replace function
data['clientAge'] = data['clientAge'].str.replace('[' , '')

data['lengthOfContract'] = data['lengthOfContract'].str.replace(']' , '')


#using the lower function to change the item to lowcase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns 

#df = df.drop('columnname, axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)

data = data.drop(['Year', 'Month'], axis = 1)

#export into CSV

data.to_csv('Valueinc_cleaned.csv', index = False)

























