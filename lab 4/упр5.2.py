import numpy as np
import re
data = open("Cell_culture.txt", "r").readlines()
date = []
name = []
volume = []
comment = []
for i in range(len(data)):
    buf = data[i].split()
    date.append((buf[0]))
    name.append((buf[1]))
    volume.append((buf[2]))
    comment.append((buf[3]))
summ=0
names_9_apr = []
for i in range(len(data)):
    if date[i] == '5-Apr':
        summ += int(volume[i])
    elif date[i] == '9-Apr':
        names_9_apr.append(name[i])
print(summ)
print(names_9_apr)