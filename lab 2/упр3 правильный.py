import numpy as np
import matplotlib.pyplot as plt
data = open("mutant.txt", "r").readlines()
data1 = open("wild_type.txt", "r").readlines()
x= []
y =[]
x1 = []
y11 = []
x2 = []
y12 = []
lenn = len(data)
lenn1 = len(data1)

def correlation (x,y):
    dsx= np.std(x)
    dsy= np.std(y)
    n=len(x)
    a=[]
    for i in range (n):
        element=((x[i]-np.mean(x))/dsx)*((y[i]-np.mean(y))/dsy)
        a.append(element)
    S=np.sum(a)
    r=1/n*S
    return r

for i1 in range(lenn):
    buf = data[i1].split()
    x1.append(float(buf[0]))
    y11.append(float(buf[1]))

for i2 in range(lenn1):
    buf1 = data1[i2].split()
    x2.append(float(buf1[0]))
    y12.append(float(buf1[1]))
x01 = [1, 2, 3, 4, 5]
y01 = [0.69123, 0.92137, 0.515, 0.712, 0.125]
x02 = np.random.rand(100)
y02 = np.random.rand(100)

data = 10 * np.random.rand(100)
x03 = np.sort(data)
epsilon3 = np.random.rand(100)
y03 = (x03-5)**2 / 10 + epsilon3 - 0.5

r11=correlation(x1,y11)
r12=correlation(x1,y12)

r01=correlation(x01,y01)
r02=correlation(x02,y02)
r03=correlation(x03,y03)

print('mutant: r =', r11)
print('wild_type: r =', r12)
print('Малое количество точек: r =', r01)
print('Переменные не связаны между собой: r =', r02)
print('Переменная: r =', r03)

plt.show()