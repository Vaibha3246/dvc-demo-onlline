import numpy as np
import pandas as pd
import os  
df=pd.read_csv('C:/Users/vaibh/Downloads/Customer Segmentation.csv')
df.drop(columns=['ID'],inplace=True)
df=df[df['Age']>30]
df=df[df['Work_Experience']>1]
df.to_csv(os.path.join('data','customer.csv')) 
