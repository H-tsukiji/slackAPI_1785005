import csv,codecs
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


#csvデータを読み込む関数
#返り値はbot1{{time:ti,text:""},...,}の配列になる
def Reading_csvfile():
    f = codecs.open("dataset2.csv","r",encoding="utf-8")
    reader = csv.reader(f)
    csv_data = []
    for i,row in enumerate(reader):
        botname = row[0]
        del row[0]
        csv_data.append(row)
    f.close()
    return csv_data

csv_list = Reading_csvfile()
print(csv_list)
data_list = np.array(csv_list)
data_list = data_list.astype(np.int)

result = cos_sim_matrix(data_list)

#np.savetxt('botdata_cosresult.csv', result, delimiter=',')

'''
実行例
[[1,2,3],[4,5,6],[7,8,9]]の場合
以下の結果が得られる
         [1,2,3]      [4,5,6]     [7,8,9]
       ------------------------------------------
[1,2,3]|[[ 1.          0.95941195  0.99819089]
[4,5,6]| [ 0.95941195  1.          0.97463185]
[7,8,9]| [ 0.99819089  0.97463185  1.        ]]



resultの中身
[ 1.          0.34846728  0.41063772  0.30885039  0.31510171  0.32043868
  0.24947389]
[ 0.34846728  1.          0.49839808  0.34982496  0.37083265  0.33512535
  0.31663725]
[ 0.41063772  0.49839808  1.          0.32077836  0.27189386  0.43460942
  0.27737926]
[ 0.30885039  0.34982496  0.32077836  1.          0.49145208  0.30863153
  0.18839029]
[ 0.31510171  0.37083265  0.27189386  0.49145208  1.          0.32594143
  0.30181799]
[ 0.32043868  0.33512535  0.43460942  0.30863153  0.32594143  1.
  0.39566203]
[ 0.24947389  0.31663725  0.27737926  0.18839029  0.30181799  0.39566203
  1.        ]





'''