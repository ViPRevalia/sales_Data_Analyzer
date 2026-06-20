import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales=pd.read_csv("pandas/sales_data.csv")

dt=pd.DataFrame(sales)
dt["DATE"] = pd.to_datetime(dt["DATE"])
# print(dt.head())
# print(dt.shape)
# print(dt.info())
# print(dt.describe())
# print(dt.isnull().sum())

dt["REVENUE"]=dt["QUANTITY"]*dt["PRICE"]
print("Total revenue : ",dt["REVENUE"].sum())
print()
dt["Profit"]=np.where(
    dt["REVENUE"]>5000,
    dt["REVENUE"]*0.2,
    dt["REVENUE"]*0.3
)
print(dt.head())
print()
total_sales=np.sum(dt["REVENUE"])
print("Total sales= ",total_sales)
print()
Avg_sales=np.mean(dt["REVENUE"])
print("Averge sales= ",Avg_sales)
print()
Category_sales=dt.groupby("CATEGORY")["REVENUE"].sum()
print("Category_sales = ",Category_sales)
print()
Product_sales=dt.groupby("PRODUCT")["REVENUE"].sum()
print("Product_Sales = ",Product_sales)
print()
best_selling=dt.groupby("PRODUCT")["QUANTITY"].sum()
print("Selling Rate = ",best_selling)
print()
dt["MONTH"]=dt["DATE"].dt.month
Monthly_sales=dt.groupby("MONTH")["REVENUE"].sum()
print("Monthly sales= ",Monthly_sales)
print()
plt.figure(figsize=(10,5))
Monthly_sales.plot(marker="o")
plt.title("Month sales trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

summary=pd.DataFrame({
    "Total sales":[dt["REVENUE"].sum()],
    "Average sales":[dt["REVENUE"].mean()],
    
})
summary.to_excel("sales_report.xlsx",index=False)
print("Report saved")
