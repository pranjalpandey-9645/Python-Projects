n1 = int(input("Enter number of employees at location 1: "))
avg1 = int(input("Enter average salary at location 1: "))

n2 = int(input("Enter number of employees at location 2: "))
avg2 = int(input("Enter average salary at location 2: "))

#Calculating combined arithmetic mean
combined_mean = (n1 * avg1 + n2 * avg2) / (n1 + n2)

# Output
print("The combined average salary is:", combined_mean)