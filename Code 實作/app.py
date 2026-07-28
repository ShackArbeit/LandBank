import numpy as np
def minmax_scale(values):
    arr = np.asarray(values,dtype=float)
    if arr.ndim!=1:
        raise ValueError('只接受一維資料')
    if arr.size ==0:
        return arr.copy()
    minimum = arr.min()
    maximum = arr.max()
    if maximum == minimum:
        return np.zeros_like(arr)
    return (arr-minimum)/(maximum-minimum)

values = [10, 20, 30, 40, 50]
result = minmax_scale(values)
print(result)