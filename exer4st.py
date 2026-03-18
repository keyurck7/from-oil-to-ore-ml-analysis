import statistics as st

data = [5,7,8,7,10,6,9,8,7,6]

data_range = max(data) - min(data)
variance = st.pvariance(data)   # variance
std_dev = st.pstdev(data)       # deviation

print("Range:", data_range)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
