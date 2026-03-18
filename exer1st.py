data = [5, 7, 8, 7, 10, 6, 9, 8, 7, 6]

# Mean
mean = sum(data) / len(data)

# Median
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 1:
    median = sorted_data[n // 2]
else:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

# Mode
counts = {}
for x in data:
    counts[x] = counts.get(x, 0) + 1
print(counts)
mode = max(counts, key=counts.get)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
