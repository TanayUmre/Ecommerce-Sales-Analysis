plt.figure(figsize=(12,6))
plt.plot(ms.index.astype(str),ms.values,marker='o',linestyle='-')
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend of Ecommerce Platform")
plt.xlabel("Month")
plt.ylabel("Total Sales in the Month")
plt.grid()
plt.show()