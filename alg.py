class Checker:
    def __init__(self, graph):
        self.graph = graph

    def check_bipartite_graph(self):
        a = []
        b = []
        visited = [1]
        q = [(1, 1)]
        flag = True
        while len(q) != 0:
            current = q.pop(0)
            for point in self.graph.points[current[0]]:
                if visited.count(point) == 0:
                    visited.append(point)
                    q.append((point, current[0]))
            if a.count(current[1]) == 0:
                for point in a:
                    if self.graph.points[current[0]].count(point) != 0:
                        flag = False
                        break
                a.append(current[0])
            elif b.count(current[1]) == 0:
                for point in b:
                    if self.graph.points[current[0]].count(point) != 0:
                        flag = False
                        break
                b.append(current[0])
            else:
                flag = False
            if not flag:
                break

        if flag:
            print('Y')
            a.sort()
            b.sort()
            print(a, b, sep='\n')
            f = open("out.txt", "a")
            f.write("Y\n" + str(a) + "\n" + str(b) + "\n")
            f.close()
        else:
            print('N')
            f = open("out.txt", "a")
            f.write("N\n")
