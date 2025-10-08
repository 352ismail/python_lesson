import pandas as pd

# print(pd.__version__)

#series : it is one diamentional labeled array 



# creating a series 

daily_steps = [5234, 6890, 7892, 4567, 9123, 10012, 8450]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = pd.Series(daily_steps, index = days)
print(steps)

# Print total, average, max, and min steps.
print(f"total steps : {sum(steps)}")
print(f"Average : {sum(steps)/len(steps)}")
print(f"maximum steps : {steps.max()}")
print(f"minimum steps : {steps.min()}")

# Find which day you walked the most.
print(f"the day you walked the most: {steps[steps == steps.max()].index[0]}")

# Check how many days you walked more than 8000 steps.
days = steps[steps > 8000].index.values
print(f"Days where you walked more than 8000 steps: {days}")

# Add 500 extra steps to each day to simulate calibration adjustment.
# this can be done using dataframes 

# calibration = steps[steps*5000]
# print(calibration)