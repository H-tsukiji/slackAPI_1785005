import numpy as np

def ascore(x):
    xmean = x.mean()
    xstd = np.std(x)
    zscore = (x-xmean)/xstd
    return zscore

arr = np.asarray([1,2,3])
print(ascore(arr))
