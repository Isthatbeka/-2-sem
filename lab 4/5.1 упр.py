import numpy as np
data = np.array([
    [7, 1, 4],
    [8, 6, 5],
    [1, 2, 3]])
sort1=np.sort(data, axis=0)
trans=sort1.T
hor=np.hstack((sort1, trans))
ver=np.vstack((sort1,trans))
f=np.concatenate((sort1, trans), axis=None)
print('отсортированные столбцы: ', '\n', sort1)
print('транспонированный массив: ', '\n', trans)
print('вертикальное объединение: ', '\n', ver)
print('горизонтальное объединение: ', '\n', hor)
print('объединение без оси: ', '\n', f)
