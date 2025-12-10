import math
l1=[56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
l2=[x for x in l1 if not math.isnan(x)]
print(l2)