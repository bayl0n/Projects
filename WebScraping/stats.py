import numpy
from scipy import stats

speed = [99, 86, 88, 111, 86, 94, 78, 77, 85, 86]

x = stats.mode(speed)

print(x)
print(numpy.var(speed))