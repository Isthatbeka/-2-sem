import numpy as np
square = np.array([
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]])
sumcol = square.sum(axis=0)
sumline = square.sum(axis=1)
s1 = square[:2, :2]
s11 = s1.sum(axis=1)
s12 = s11.sum(axis=0)
s2 = square[:2, 2:]
s21 = s2.sum(axis=1)
s22 = s21.sum(axis=0)
s3 = square[2:, :2]
s31 = s3.sum(axis=1)
s32 = s31.sum(axis=0)
s4 = square[2:, 2:]
s41 = s4.sum(axis=1)
s42 = s41.sum(axis=0)
s5 = square[1: 3:, 1: 3:]
s51 = s5.sum(axis=1)
s52 = s51.sum(axis=0)
print('столбцы: ', sumcol)
print('строки: ', sumline)
print('левый верхний: ', s12)
print('правый верхний: ', s22)
print('левый нижний: ', s32)
print('правый верхний: ', s42)
print('центр: ', s52)