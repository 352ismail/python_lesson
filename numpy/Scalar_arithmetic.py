import numpy as np



# A shopkeeper sells notebooks for Rs. 50 each.
# Create a NumPy array of quantities [2, 5, 10, 20] and calculate the total cost for each order.
quantities =np.array([2, 5, 10, 20])
cost_for_each = 50
total = quantities * cost_for_each
print(total)



# A car consumes 0.08 liters of fuel per km.
# Given distances [10, 25, 50, 100], calculate the fuel used for each trip.
fuel_average_per_km = 0.8
distances = np.array([10, 25, 50, 100])
toatal_fuel_consumed = distances * fuel_average_per_km
print(f'{toatal_fuel_consumed}')





# A person invests Rs. 100,000 at a bank with 5% annual interest.
# Use NumPy to calculate the amount after 1, 2, 3, 4, 5 years.
invesment = 100000
interest_rate = 0.5
years = np.array([1,2,3,4,5])
invesment_for_years = years * (invesment/100) * interest_rate
print(invesment_for_years)