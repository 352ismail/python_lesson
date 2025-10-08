import numpy as np 

# sales = np.array([10, 50, 12, 18, 20, 17, 16])
# total_sale = np.sum(sales)


# #Find the total sales of the week.
# print(f"Total sales of the week: {total_sale}")

# #Find the average daily sales.
# avg = np.average(sales)
# print(f"average: {avg}")


# # Find the day with maximum sales.
# max_day = np.argmax(sales)+1
# print(f"Max sale on : {max_day}")

# # Find the day with minimum sales.

# max_day = np.argmin(sales)+1
# print(f"Min sale on : {max_day}")



# scores = np.array([
#     #subjects
#     #maths, english, physics
#     [85, 78, 92], # akram
#     [88, 76, 95], # izaaz
#     [90, 82, 87], # ali
#     [70, 65, 89]  # imran
# ])

# #Find the average score of each student.

# averagre = np.average(scores, axis=1)
# print(f"average of each student: {averagre}")

# # Find the average score of each subject.
# avg_subject = np.average(scores, axis = 0 )
# print(f"the average of each subject is: {avg_subject}")

# # Find the highest score in the class.
# max_number = np.max(scores)
# print(f"topped on: {max_number}")


# # Find the lowest score in the class.
# min_number = np.min(scores)
# print(f"minimun numbers got: {min_number}")



# temperature = np.array([32.5, 17.0, 34.2, 35.1, 33.8, 18.0, 34.7])

# #Find the average weekly temperature.
# average_temp = np.average(temperature)
# print(f"average temperature: {average_temp:.2f}")
# # Find the temperature variance and standard deviation.
# variance = np.var(temperature)
# print(f"variance: {variance}")


# std = np.std(temperature)
# print(f"Standard deviation: {std}")




orders = np.array([
    #p1,p2,p3
    [5, 3, 2],   # Customer 1 ordered
    [2, 0, 1],   # Customer 2 ordered
    [4, 2, 3],   # Customer 3 ordered
    [1, 10, 1]    # Customer 4 ordered
])


# Find the total number of each product ordered.
each_product_ordered = np.sum(orders, axis=0)
print(f"each product ordered: {each_product_ordered}")
# Find the total number of orders by each customer.
each_customer_ordered = np.sum(orders, axis=1)
print(f"each customer ordered: {each_customer_ordered}")

# Find the average number of items ordered per customer.
each_customer_ordered = np.sum(orders, axis=1)
print(f"average customer ordered: {np.average(each_customer_ordered)}")

# Find the customer who ordered the most items.
customer = np.argmax(each_customer_ordered)+1
print(f"Customer {customer} order the most items")
