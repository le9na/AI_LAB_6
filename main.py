class IDS:
    def __init__(self, start, goal, size=12):
        self.N = size  # number of vertices in the graph
        self.G = [[False] * size for _ in range(size)]
        self.start_city = start
        self.goal = goal
        self.visited = [False] * size
        self.level = [0] * size
        self.limit = 0
        self.setup_graph()
        self.parent = [-1] * size

    def setup_graph(self):
        edges = [(0, 1),
                 (0, 8),
                 (0, 4),
                 (1, 2),
                 (1, 3),
                 (2, 6),
                 (3, 4),
                 (3, 5),
                 (6, 7),
                 (8, 9),
                 (9, 10),
                 (10, 11)]
        for (i, j) in edges:
            self.G[i][j] = self.G[j][i] = True

    def ids(self):
        while not self.dls():
            self.limit += 1
            self.visited = [False] * self.N
            self.level = [0] * self.N
            self.parent = [-1] * self.N

    def dls(self):
        stack = [self.start_city]
        self.visited[self.start_city] = True
        while stack:
            current = stack.pop()
            if current == self.goal:
                self.print_path(current)
                print(f"Cities visited before finding the goal at depth {self.limit}:\nTop of stack ->",
                      [self.ret_city(city) for city in range(self.N) if
                       self.visited[city] and self.level[city] == self.limit])
                return True
            if self.level[current] < self.limit:
                children = [i for i in range(self.N) if self.G[current][i] and not self.visited[i]]
                for neighbor in reversed(children):
                    stack.append(neighbor)
                    self.visited[neighbor] = True
                    self.level[neighbor] = self.level[current] + 1
                    self.parent[neighbor] = current
        print("\n+------------------------------------------+")
        print(f"\nCities visited at depth {self.limit}: ", [self.ret_city(city) for city in range(self.N) if self.visited[city]])
        return False

    def print_path(self, current):
        path = []
        while current != -1:
            path.append(current)
            current = self.parent[current]
        path.reverse()
        print("\n+------------------------------------------+")
        print(f"Goal is reached at depth {self.limit}\nPath:", " ".join(self.ret_city(city) for city in path))

    @staticmethod
    def ret_city(i):
        cities = ["Buraydah", "Unayzah", "AlZulfi",
                "Al-Badai", "Riyadh-Alkhabra", "AlRass",
                "UmSedrah", "Shakra", "Al-Bukayriyah",
                "Sheehyah", "Dhalfa", "Mulida"]
        return cities[i]


if __name__ == "__main__":
    for i in range(12):
        print(f"[{i}]: {IDS.ret_city(i)}")

    print("\nChoose a city number to start:")
    print("Input: ", end="")
    chosen_city = int(input())

    print("\nChoose a city number for the goal: ")
    print("Input: ", end="")
    goal = int(input())

    ids = IDS(chosen_city, goal)
    ids.ids()

