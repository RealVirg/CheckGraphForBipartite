class Graph:
    def __init__(self, count, matrix):
        self.count = count
        self.points = {}
        for line in range(count):
            self.points[line + 1] = []
        for line in range(count):
            for symbol in range(count):
                if matrix[line][symbol] == '1' and symbol != line:
                    self.points[line + 1].append(symbol + 1)

    def __str__(self):
        return str(self.points)


class ReadGraphsFromFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def reading(self):
        graph_list = []
        with open(self.file_name, 'r') as f:
            while True:
                r = f.readline()
                if not r:
                    break
                if len(r.split(" ")) > 1:
                    print("incorrect input")
                    quit()
                try:
                    r = int(r)
                except ValueError:
                    print("incorrect input")
                    quit()

                i = 0
                matrix = []
                while i < r:
                    r1 = f.readline()
                    if not r1 or (len(r1) != r and r1[-1] != "\n") or (len(r1) != r + 1 and r1[-1] == "\n"):
                        print("incorrect input")
                        quit()
                    try:
                        int(r1)
                    except ValueError:
                        print("incorrect input")
                        quit()
                    matrix.append(r1)
                    i += 1

                graph_list.append(Graph(r, matrix))

        return graph_list
