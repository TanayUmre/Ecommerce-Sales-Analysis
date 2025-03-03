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

df["Year-Month"]=df["Order Date"].dt.to_period("M")   # This will show the monthy trend of the sales 
ms=df.groupby("Year-Month")["Sales"].sum()
plt.figure(figsize=(12,6))
plt.plot(ms.index.astype(str),ms.values,marker='o',linestyle='-')
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend of Ecommerce Platform")
plt.xlabel("Month")
plt.ylabel("Total Sales in the Month")
plt.grid()
plt.show()
# This will show the monthly sales trend of the ecommerce platform

prolar=df.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()  # This will show the top 10 products with highest sales
plt.figure(figsize=(10,5))
plt.bar(prolar['Product Name'],prolar["Sales"],color='skyblue')
plt.title("Top 10 best selling products")
plt.ylabel("Total Sales")
plt.xlabel("Product Name")
plt.xticks(rotation=45,ha="right",fontsize=6)
plt.show()
# This will show the top 10 best selling products

prosma=df.groupby("Product Name")["Sales"].sum().nsmallest(10).reset_index()  # This will show the top 10 products with lowest sales
plt.figure(figsize=(10,5))
plt.bar(prosma['Product Name'],prosma["Sales"],color='skyblue')
plt.title("Top 10 least selling products")
plt.ylabel("Total Sales")
plt.xlabel("Product Name")
plt.xticks(rotation=45,ha="right",fontsize=6)
plt.show()
# This will show the top 10 least selling products

saleregion=df.groupby("Region")["Sales"].sum()   # This will show the sales done by regions
custop=df.groupby("Customer Name")["Sales"].sum().nlargest(10).reset_index()  # This will show the top 10 customers with most orders
saleregion.plot(kind='pie',autopct='%1.1f%%',figsize=(8,8),colormap='viridis')
plt.title("Sales distribution by Region")
plt.ylabel("")
plt.show()
# This will show the sales distribution by region

cuslow=df.groupby("Customer Name")["Sales"].sum().nsmallest(10).reset_index()   # This will show the top 10 customers with least orders
plt.figure(figsize=(10,5))
plt.bar(custop["Customer Name"].astype(str),custop["Sales"],color='red')
plt.title("Top 10 customers with most orders")
plt.ylabel("Total Orders")
plt.xlabel("Customer Name")
plt.xticks(rotation=70,ha="right")
plt.show()
# This will show the top 10 customers with most orders placed

plt.figure(figsize=(10,5))
plt.bar(cuslow["Customer Name"].astype(str),cuslow["Sales"],color='indigo')
plt.title("Top 10 customers with lowest orders")
plt.ylabel("Total Orders")
plt.xlabel("Customer Name")
plt.xticks(rotation=70,ha="right")
plt.show()
# This will show the top 10 customers with lowest orders placed

ctsa=df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
ctsa.plot(kind='bar',color='magenta')
plt.title("Sales by Product Category")
plt.ylabel("Total Sales")
plt.xlabel("Category")
plt.xticks(rotation=0,ha="right")
plt.show()
# This will show the sales by product category

ctpro=df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
ctpro.plot(kind='bar',color='orange')
plt.title("Profit by Product Category")
plt.ylabel("Total Profit")
plt.xlabel("Category")
plt.xticks(rotation=0,ha="right")
plt.show()
# This will show the sales by product category

days=df["Order Date"].dt.day_name().value_counts()
plt.figure(figsize=(7,7))
days.plot(kind='pie',autopct='%1.1f%%')
plt.title('Orders Distribution by the Day of the Week')
plt.ylabel("")
plt.show()
# This will show on daywise share of orders placed

custord=df["Customer ID"].value_counts()
plt.figure(figsize=(10,5))
plt.hist(custord,bins=30,color="blue",edgecolor="black")
plt.title("Customer Purchase Frequency Distribution",fontsize=14)
plt.xlabel("Number of Orders",fontsize=12)
plt.ylabel("Number of Customers",fontsize=12)
plt.grid()
plt.show()
# This will show the distribution of customer purchase frequency

state=df["State"].value_counts()
ts=state.nlargest(5)
ls=state.nsmallest(5)

plt.figure(figsize=(10,5))
plt.bar(ts.index,ts.values,color="green")
plt.title("Top 5 States with Most Orders Placed")
plt.xlabel("States")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.show()
# This will show the top 5 states with most orders placed

plt.figure(figsize=(10,5))
plt.bar(ls.index,ls.values,color="blue")
plt.title("Top 5 States with Least Orders Placed")
plt.xlabel("States")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.show()
# This will show the top 5 states with least orders placed

shipmode=df["Ship Mode"].value_counts()
plt.figure(figsize=(7,7))
plt.pie(shipmode,labels=shipmode.index,autopct="%1.1f%%",startangle=140)
plt.title("Order Distribution by Ship Mode")
plt.ylabel("")
plt.show()
# This will the distrution of various shipmodes

year=df["Year"].value_counts()
plt.figure(figsize=(7,7))
plt.pie(year,labels=year.index,autopct="%1.1f%%",startangle=0)
plt.title("Year-wise Order Distribution")
plt.ylabel("")
plt.show()
# This will show the year-wise distribution of orders 

yp=df.groupby("Year")["Profit"].sum()
plt.figure(figsize=(7,7))
plt.pie(yp,labels=yp.index,autopct="%1.1f%%",startangle=0)
plt.title("Yearly Profit Distribution")
plt.ylabel("")
plt.show()
# This will show the yearly profit distribution

yearwiseprofit=df.groupby(["State","Year"])["Profit"].sum().unstack()
sp=yearwiseprofit.sum(axis=1).nlargest(5).index
ssp=yearwiseprofit.loc[sp]
ssp.plot(kind="bar",colormap="viridis",edgecolor="black")
plt.title("Top 5 States with Highest Profit Over the Years",fontsize=14)
plt.xlabel("States",fontsize=12)
plt.ylabel("Profit",fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Year")
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.show()
# This will show the profit done in top 5 states with most profit over 4 years

lsp=yearwiseprofit.sum(axis=1).nsmallest(5).index
lssp=yearwiseprofit.loc[lsp]
lssp.plot(kind="bar",colormap="viridis",edgecolor="black")
plt.title("Top 5 States with Least Profit Over the Years",fontsize=14)
plt.xlabel("States",fontsize=12)
plt.ylabel("Profit",fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Year")
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.show()