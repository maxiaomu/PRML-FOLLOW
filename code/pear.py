import numpy as np
from scipy.stats import pearsonr
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cosine
from sklearn.preprocessing import StandardScaler

# 设定向量长度，均为100
n = 100
x1 = np.random.random_integers(0,10,(n,1))
x2 = np.random.random_integers(0,10,(n,1))
x3 = np.random.random_integers(0,10,(n,1))

p12 = 1-pearsonr(x1,x2)[0][0]
p13 = 1-pearsonr(x1,x3)[0][0]
p23 = 1-pearsonr(x2,x3)[0][0]

d12 = (euclidean(x1,x2)**2)/(2*n)
d13 = (euclidean(x1,x3)**2)/(2*n)
d23 = (euclidean(x2,x3)**2)/(2*n)

c12 = cosine(x1,x2)
c13 = cosine(x1,x3)
c23 = cosine(x2,x3)

print('\n原始数据，没有标准化\n')
print('                  x1&x2  x2&x3  x1&x3')
print('pearson:        ',np.round(p12,decimals=4),np.round(p13,decimals=4),np.round(p23,decimals=4))
print('cos:            ',np.round(c12,decimals=4),np.round(c13,decimals=4),np.round(c23,decimals=4))
print('euclidean sq:   ',np.round(d12,decimals=4),np.round(d13,decimals=4),np.round(d23,decimals=4))

x1_n = StandardScaler().fit_transform(x1)
x2_n = StandardScaler().fit_transform(x2)
x3_n = StandardScaler().fit_transform(x3)

p12_n = 1-pearsonr(x1_n,x2_n)[0][0]
p13_n = 1-pearsonr(x1_n,x3_n)[0][0]
p23_n = 1-pearsonr(x2_n,x3_n)[0][0]

d12_n = (euclidean(x1_n,x2_n)**2)/(2*n)
d13_n = (euclidean(x1_n,x3_n)**2)/(2*n)
d23_n = (euclidean(x2_n,x3_n)**2)/(2*n)

c12_n = cosine(x1_n,x2_n)
c13_n = cosine(x1_n,x3_n)
c23_n = cosine(x2_n,x3_n)

print('\n标准化后的数据：均值=0，标准差=1\n')
print('                  x1&x2  x2&x3  x1&x3')
print('pearson:        ',np.round(p12_n,decimals=4),np.round(p13_n,decimals=4),np.round(p23_n,decimals=4))
print('cos:            ',np.round(c12_n,decimals=4),np.round(c13_n,decimals=4),np.round(c23_n,decimals=4))
print('euclidean sq:   ',np.round(d12_n,decimals=4),np.round(d13_n,decimals=4),np.round(d23_n,decimals=4))
