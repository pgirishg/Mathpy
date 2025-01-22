import math

#sample data
data=[1,19,2,18,3,17,4,16,5,15,6,14,7,13,8,12,9,11,10]

#calculate mean
mean=sum(data)/len(data)
print("Mean:",mean)

#calculate variance
variance=sum((x-mean)**2 for x in data)/len(data)
print("Variance:",variance)

#calculate standard deviation
std_dev=math.sqrt(variance)
print("Standard Deviation:",std_dev)




