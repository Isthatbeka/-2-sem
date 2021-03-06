import numpy as np
import matplotlib.pyplot as plt
data = open("mutant.txt", "r").readlines()
data1 = open("wild_type.txt", "r").readlines()
con1 = []
con = []
res = []
res1 = []
lenn = len(data)
lenn1 = len(data1)
for i1 in range(lenn):
    buf = data[i1].split()
    con.append(float(buf[0]))
    res.append(float(buf[1]))
plt.scatter(con,res,s=5,c="purple",label='mutant')
for i2 in range(lenn1):
    buf1 = data1[i2].split()
    con1.append(float(buf1[0]))
    res1.append(float(buf1[1]))
plt.scatter(con1,res1,s=1,c="red",label='wild type')
plt.title('fluorescence')
plt.xlabel('protein')
plt.ylabel('response')
plt.legend(loc='best', fontsize=9)

plt.show()
