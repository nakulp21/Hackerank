"""
from statistics import mean, mode, median
n = int(input())
arr = [map(int, input().split())]

avg = mean(arr)
med = median(arr)
mod = mode(arr)[0]

print("{:.1f}".format(avg))
print("{:.1f}".format(med))
print(mod)
"""
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))




