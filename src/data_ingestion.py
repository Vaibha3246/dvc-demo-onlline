import pandas as pd
import numpy as np
import os
df=pd.read_csv('C:/Users/vaibh/Downloads/Customer Segmentation.csv')
df.drop(columns=['ID'],inplace=True)
df = df[(df['Age'] > 30) & (df['Work_Experience'] > 1)]

df.to_csv(os.path.join('data','employee.csv'),index=False)