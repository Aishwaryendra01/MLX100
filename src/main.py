print("hello Machine leaning environment is ready....")

# step : preprocesing 
import pandas as pd 
import numpy as np

df = pd.read_csv('../data/placement.csv')
# this is preprocessing of the data using the pandas loc /iloc function which is used for slicing
# here we take the relevant dta from the huge data set
df = df.iloc[:,1:]
print(df)

#step : EDA Eploratoey data analysis
# now we will use the library matplotlib to for the EDA purpose
import matplotlib.pyplot as plt

plt.scatter(df['cgpa'],df['iq'],c=df['placement'])




