data = [5,7,8,7,10,6,9,8,7,6]

# Range
data_range = max(data) - min(data)

# Variance (population)
mean = sum(data)/len(data)
variance = sum((x-mean)**2 for x in data) / len(data)

# Standard deviation
std_dev = variance**0.5

print("Range:", data_range)
print("Variance:", variance)
print("standard deviation:", std_dev)
