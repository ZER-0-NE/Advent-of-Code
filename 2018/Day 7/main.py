import networkx as nx
from string import ascii_uppercase

dic = {}

Graph = nx.DiGraph()
Graph.add_edges_from([(x.split()[1], x.split()[7]) for x in open('data.txt').readlines()])

# print(Graph.edges())

res = ''.join(nx.lexicographical_topological_sort(Graph))

print(f"1. {res}")
