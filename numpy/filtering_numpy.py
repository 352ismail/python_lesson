import numpy as np

# Boolean mask 
salaries = np.array([35000, 42000, 50000, 28000, 75000, 60000, 45000])

#Get all employees earning more than 50,000.
senior_devs = salaries[salaries>50000]
print(senior_devs)

#Get all employees earning less than 40,000.
intermediate_devs = salaries[salaries<40000]
print(intermediate_devs)

#Get all employees earning between 40,000 and 60,000.
anonymous = salaries[(salaries>40000) & (salaries<60000)]
print(anonymous)




ratings = np.array([2.5, 4.8, 3.2, 5.0, 4.1, 2.9, 4.5])
# Get all products rated 4.0 or higher.
high_rating = ratings[ratings>4.0]
print(high_rating)

# Get all products rated below 3.0.

low_ratings = ratings[ratings<3.0]
print(low_ratings)




temps = np.array([25, 32, 40, 22, 19, 35, 28])
# Get all days with temperature above 30.
indices = np.nonzero(temps > 30)
print(indices)

# Get all days with temperature below or equal to 20.





