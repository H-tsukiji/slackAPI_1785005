import numpy as np

def cos_sim_matrix(matrix):
    """
    item-feature 行列が与えられた際に
    item 間コサイン類似度行列を求める関数
    """
    d = matrix @ matrix.T  # item-vector 同士の内積を要素とする行列
    # コサイン類似度の分母に入れるための、各 item-vector の大きさの平方根
    norm = (matrix * matrix).sum(axis=1, keepdims=True) ** .5
    # それぞれの item の大きさの平方根で割っている
    return d / norm / norm.T

a = np.array([[1,2,3],[4,5,6],[7,8,9],[987,675,777],[0,2789,9]])
result = cos_sim_matrix(a)
print(result)
'''
実行例
[[1,2,3],[4,5,6],[7,8,9]]の場合
以下の結果が得られる
         [1,2,3]      [4,5,6]     [7,8,9]
       ------------------------------------------
[1,2,3]|[[ 1.          0.95941195  0.99819089]
[4,5,6]| [ 0.95941195  1.          0.97463185]
[7,8,9]| [ 0.99819089  0.97463185  1.        ]]

'''