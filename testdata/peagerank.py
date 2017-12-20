# -*- coding: utf-8 -*-
import networkx as nx

#有向グラフのインスタンスを生成
g = nx.DiGraph()

#ノードを追加する ※ソーシャルグラフなら人がノードになることが多い
g.add_node("user1")
g.add_node("user2")
g.add_node("user3")                                                                                                                     
g.add_node("user4")
g.add_node("user5")
g.add_node("user6")
g.add_node("user7")

#ノード間の矢印を加えていく
#user1
g.add_edge("user1","user2")
g.add_edge("user1","user3")
g.add_edge("user1","user4")
g.add_edge("user1","user5")
g.add_edge("user1","user6")
g.add_edge("user1","user7")
#user2
g.add_edge("user2","user1")
g.add_edge("user2","user4")
g.add_edge("user2","user5")
g.add_edge("user2","user6")
g.add_edge("user2","user7")
#user3
g.add_edge("user3","user1")
g.add_edge("user3","user4")
g.add_edge("user3","user5")
g.add_edge("user3","user6")
g.add_edge("user3","user7")
#user4
g.add_edge("user4","user1")
g.add_edge("user4","user2")
g.add_edge("user4","user3")
g.add_edge("user4","user5")
#user5
g.add_edge("user5","user1")
g.add_edge("user5","user2")
g.add_edge("user5","user3")
g.add_edge("user5","user7")
#user6
g.add_edge("user6","user1")
g.add_edge("user6","user2")
g.add_edge("user6","user3")
g.add_edge("user6","user4")
g.add_edge("user6","user5")
#user7
g.add_edge("user7","user1")
g.add_edge("user7","user2")
g.add_edge("user7","user3")
g.add_edge("user7","user5")

#pagerank値の計算
pr=nx.pagerank(g,alpha=0.85)

#pagerank値の計算(numpyを利用)
prn=nx.pagerank_numpy(g,alpha=0.85)

print("-----pagerank(numpy)-----")
print(prn)