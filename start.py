import graph
import alg


reader = graph.ReadGraphsFromFile("in.txt")

graph_list = reader.reading()

f = open("out.txt", "w")
f.close()
for g in graph_list:
    a = alg.Checker(g)
    a.check_graph_for_bipartite()


