import numpy as np 
# Scenario: You manage sales for 5 stores across 7 days.
sales = np.random.randint(1000, 5000, size=(5, 7))
print(sales)



# Find total weekly sales per store.
total_weekly_sales = sales.sum(axis=1)
print(total_weekly_sales)

# Find average daily sales across all stores.
daily_sale = sales.mean()
print(f"average daily sale: {daily_sale}")


# Find which store had the highest total sales.
highest_sale = total_weekly_sales.max()

print(F"highest weekly sale {highest_sale}")

# Sort stores by total sales (descending).
print(f"sorted values: {np.sort(total_weekly_sales)[::-1]}")
