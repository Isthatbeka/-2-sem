import matplotlib.pyplot as plt
plt.figure(figsize=(15, 5))
data = open("chromo.txt", "r").readlines()
x = []
value = []
sp1 = plt.subplot(111)
for i in range(1 ,len(data),1):
    buff = data[i].split()
    x.append(float(buff[0]))
    value.append(float(buff[1]))
plt.plot(x,value)
plt.title('fluorescence')
plt.xlabel('time')
plt.ylabel('signal')
plt.show()
