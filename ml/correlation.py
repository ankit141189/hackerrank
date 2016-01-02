import math
import numpy

def mean(data_list):
	return float(sum(data_list)) / len(data_list)

def covariance(data_list_1, data_list_2):
	product_list = [x * y for (x,y) in zip(data_list_1, data_list_2)]
	return mean(product_list) - mean(data_list_1) * mean(data_list_2)

X = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
Y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

print covariance(X,Y) / (math.sqrt(covariance(X, X)) * math.sqrt(covariance(Y, Y)))
print numpy.corrcoef(X, Y)
