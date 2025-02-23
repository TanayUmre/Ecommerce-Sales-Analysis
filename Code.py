import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file="C:\\Users\\asus\\Desktop\\ITW Lab Assignment\\Ecommerce-Sales-Analysis\\ecommercedashboard\\Ecommerce Sales Analysis.xlsx"
df=pd.read_excel(file)

df["Order Date"]=pd.to_datetime(df["Order Date"],errors='coerce')
df["Ship Date"]=pd.to_datetime(df["Ship Date"],errors='coerce')
df.drop_duplicates(inplace=True)
df.fillna(0,inplace=True)

# This code is used for cleaning the data to get better output

totalsale=df["Sales"].sum()
totalprofit=df["Profit"].sum()
totalorder=df["Order ID"].nunique()
totalcustomer=df["Customer ID"].nunique()

print(f"Total Sales are : {totalsale:.4f}")
print(f"Total Profit is : {totalprofit:.4f}")
print(f"Totals Orders Placed are : {totalorder}")
print(f"Total Customers Using Ecommerce platform are : {totalcustomer}")

# This code is used to show the total sales, total profit, total orders and total customers using ecommerce platform

df["Year-Month"]=df["Order Date"].dt.to_period("M") 
# This will show the monthy trend of the sales 

ms=df.groupby("Year-Month")["Sales"].sum()
# This will show the monthly sales of the ecommerce platform

prolar=df.groupby("Product Name")["Sales"].sum().nlargest(10)
# This will show the top 10 products with highest sales

prosma=df.groupby("Product Name")["Sales"].sum().nsmallest(10)
# This will show the top 10 products with lowest sales

custop=df.groupby("Customer ID")["Sales"].sum().nlargest(10)
# This will show the top 10 customers with highest sales

cuslow=df.groupby("Customer ID")["Sales"].sum().nsmallest(10)
# This will show the top 10 customers with lowest sales

saleregion=df.groupby("Region")["Sales"].sum()
# This will show the sales done by regions