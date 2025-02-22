import pandas as pd
import numpy as np
import Matplotlib.pyplot as plt

file="C:\Users\asus\Desktop\ITW Lab Assignment\Ecommerce-Sales-Analysis\ecommercedashboard\Ecommerce Sales Analysis.xlsx"
df=pd.read_excel(file)

df["Order Date"]=pd.to_datetime(df["Order Date"],errors='coerce')
df["Ship Date"]=pd.to_datetime(df["Ship Date"],errors='coerce')
df.drop_duplicates(inplace=True)
df.fillna(0,inplace=True)

# This code is used for cleaning the data to get better output