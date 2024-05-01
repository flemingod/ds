# -*- coding: utf-8 -*-
"""Assn_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zq_RZmGg2mEPW8MR6TBxXd23i0T_QdA9

# Assignment No. 02

# Problem Statement :: Data Wrangling II
Create an “Academic performance” dataset of students and perform the following operations using Python.
1. Scan all variables for missing values and inconsistencies. If there are missing values and/or inconsistencies, use any of the suitable techniques to deal with them.
2. Scan all numeric variables for outliers. If there are outliers, use any of the suitable techniques to deal with them.
3. Apply data transformations on at least one of the variables. The purpose of this transformation should be one of the following reasons: to change the scale for better understanding of the variable, to convert a non-linear relation into a linear one, or to decrease the skewness and convert the distribution into a normal distribution.
Reason and document your approach properly.

Handling Null Values
"""

import pandas as pd #importing pandas
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
df = pd.read_csv("/content/student.csv") #reading the dataset file
df

#Checking the total count of rows of columns having null values
df.isnull().sum()

#displaying the rows with null values
df[df.isnull().any(axis=1)]

#Filling the null values with the mean of that column
df['Sem1'] = df['Sem1'].fillna(df['Sem1'].mean())
df

#Filling the null values with 0
df['Sem2'] = df['Sem2'].fillna(0)
df

#Filling the null values with "Missing" word
df['Sem3'] = df['Sem3'].fillna("Missing")
df

#Droping the rows with null values
df.dropna()

"""Understanding Outliers"""

df["Sem2"].min()

print(np.where(df["Sem2"]<20))

x=df['Sem2']
y=df['average Score']
plt.scatter(x,y)
plt.show()

x=df["Sem2"]
y=df["average Score"]
z=df["Roll No"]
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(z,x,color='r')
ax.scatter(z,y,color='g')
ax.set_xlabel('Sem2')
ax.set_ylabel('average Score')
ax.set_title('Scatter plot')
plt.show()

"""#z-score x = xi-u/sd"""

z=np.abs(stats.zscore(df['Sem1']))
z2=np.abs(stats.zscore(df['Sem2']))
z3=np.abs(stats.zscore(df['Sem3']))
z4=np.abs(stats.zscore(df['Sem4']))
print(z)

Q1=np.quantile(df['Sem1'],0.25)
Q3=np.quantile(df['Sem1'],0.75)
IQR=Q3-Q1
print("Q1 :: ",Q1)
print("Q3 :: ",Q3)
print("IQR :: ",IQR)

Q1=np.quantile(df['Sem2'],0.25)
Q3=np.quantile(df['Sem2'],0.75)
IQR=Q3-Q1
print("Q1 :: ",Q1)
print("Q3 :: ",Q3)
print("IQR :: ",IQR)
upper_2 = Q3 + 1.5*IQR
lower_2 = Q1 - 1.5*IQR
print("lower bound :: ",lower_2)
print("upper bound :: ",upper_2)

print(np.where(df['Sem2']<lower_2))

print(np.where(df['Sem2']>upper_2))

df.drop([10], inplace=True)
print(df)

Q4 = np.quantile(df['Sem4'],0.90)
Q5 = np.quantile(df['Sem4'],0.10)
IQR=Q4-Q5
print("Q4 :: ",Q4)
print("Q5 :: ",Q5)
print("IQR :: ",IQR)
upper_bound = Q4 + 1.5*IQR
lower_bound = Q5 - 1.5*IQR
print("lower bound :: ",lower_bound)
print("upper bound :: ",upper_bound)

print(df)