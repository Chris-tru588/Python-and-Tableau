# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:23:12 2023

@author: chris
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data

json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
        data = json.load(json_file)
       

#transform to data frame
loandata = pd.DataFrame(data)

#finding unique values for the purpose of the column

#describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using exp() to get the annual income
income = np.exp(loandata['log.annual.inc'])

loandata['annualincome'] = income

#working with IF statements

a = 40
b = 500

if b > a:
    print('b is greater than a')

#add more conditions
a = 40
b = 500 
c = 1000

if b > a and b < c:
    print('b is greater than a but less than c')

#what if a condition is not met
a = 40
b = 500
c = 20

if b > a and b < c:
    print('b is greater than a but less than c')
else:
    print('no conditions met')

# another condition different metrics
a = 40
b = 0
c = 30

if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
        print('b is greater than a and c')
else:
    print('no conditions met')

 #using or    
a = 40
b = 500
c = 30

if b > a or b < c:
    print('b is greater than a or less than c')
else:
    print('no conditions met')


#fico score
fico = 250

# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'very poor'
elif fico >= 400 and fico < 600:
    ficocat = 'poor'
elif fico >= 601 and fico < 660:
    ficocat = 'fair'
elif fico >= 660 and fico < 700:
    ficocat = 'good'
elif fico >= 700:
    ficocat = 'excellent'
else:
    ficocat = 'unknown'
print(ficocat)


#forloop 
fruits = ['apple', 'pear', 'banana', 'cherry']

for x in fruits:
    print(x)
    y = x + ' fruit'
    print(y)

for x in range(0,4):
    y = fruits[x]+' for sale'
    print(y)

#applying forloops to loandata

# using first 10

length = len(loandata)
ficocat = []
for x in range(0, length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'very poor'
        elif category >= 400 and category < 600:
            cat = 'poor'
        elif category >= 601 and category < 660:
            cat = 'fair'
        elif category >= 660 and category < 700:
            cat = 'good'
        elif category >= 700:
            cat = 'excellent'
        else:
            cat = 'unknown'
    except:
        cat = 'unknown'
    ficocat.append(cat)
    

ficocat = pd.Series(ficocat)


loandata['fico.category'] = ficocat

#df.loc as condition statements
#df.loc[df[columnname] condition, newcolumnname] = 'value if the condition is met'

#for interest rates a new column is wanted. rate > 0.12 then high else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans or rows by ficocategory 

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purpose = loandata.groupby(['purpose']).size()
purpose.plot.bar(color = 'red', width = 0.2)
plt.show()

#scatter plots

ypoint = loandata['annualincome']
xpoint = loandata['dti']

plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#writing to csv

loandata.to_csv('loan_cleaned.csv', index = True)




































