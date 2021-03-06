import matplotlib.pyplot as plt
import numpy as np
data = open("melting.txt", "r").readlines()
x = []
y = []
z = []
k = []
j = []
i = []
lenn = len(data)
for i1 in range(lenn):
    buf = data[i1].split()
    x.append(float(buf[0]))
    y.append(float(buf[1]))
    z.append(float(buf[2]))
    k.append(float(buf[3]))
    j.append(float(buf[4]))
    i.append(float(buf[5]))
def curve(y):
    y1new = []
    for i in range(len(y)):
        y1new.append(y[i] / (np.max(y)-np.min(y)))
    return np.clip(y1new, 0, 1)

gradesmass = [y, z, k, j, i]
for i in range (len(gradesmass)):
    grades = np.array(gradesmass[i])
    curve(grades)
    p=i+1
    sp1 = plt.subplot(2, 3, p)
    plt.plot(x, grades)
    plt.title('fluorescence ')
    plt.xlabel('temperature')
    plt.ylabel('signal')
plt.tight_layout()
plt.show()
