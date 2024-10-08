class IDS:
    def __init__(self, size, start, goal):
        self.N = size  # Number of vertices in the graph
        self.G = [[False] * size for _ in range(size)]  # Graph as an adjacency matrix
        self.sta = []  # Stack for Depth-Limited Search
        self.goal = goal  # Goal city index
        self.start_city = start  # Starting city index
        self.Acc = [False] * size  # Visited array
        self.L = [0] * size  # Levels of vertices
        self.limit = 0  # Initial depth limit
        self.path = []  # To store the path to the goal
        self.setup_graph()  # Initialize graph connections

    def setup_graph(self):
        # Undirected graph edges setup
        self.G[0][1] = self.G[1][0] = True
        self.G[0][8] = self.G[8][0] = True
        self.G[0][4] = self.G[4][0] = True
        self.G[1][2] = self.G[2][1] = True
        self.G[1][3] = self.G[3][1] = True
        self.G[2][6] = self.G[6][2] = True
        self.G[3][4] = self.G[4][3] = True
        self.G[3][5] = self.G[5][3] = True
        self.G[6][7] = self.G[7][6] = True
        self.G[8][9] = self.G[9][8] = True
        self.G[9][10] = self.G[10][9] = True
        self.G[10][11] = self.G[11][10] = True

    def search(self):
        while True:
            self.sta = [self.start_city]
            self.Acc = [False] * self.N
            self.L = [0] * self.N
            self.Acc[self.start_city] = True
            print(f"Starting search with depth limit: {self.limit}")

            if self.dls():
                print("Goal found! Path to the goal:", " -> ".join(self.path))
                return True
            if not self.inc_limit():
                print("All nodes visited without finding the goal.")
                return False
            self.limit += 1

    def dls(self):
        while self.sta:
            at = self.sta.pop()
            self.path.append(self.ret_city(at))
            
            if at == self.goal:
                return True

            print(f"\n--> At {self.ret_city(at)} [current depth: {self.L[at]}]")

            for i in range(self.N):
                if not self.Acc[i] and self.G[at][i] and self.L[at] + 1 <= self.limit:
                    self.sta.append(i)
                    self.L[i] = self.L[at] + 1
                    self.Acc[i] = True

            print("Current stack:", [self.ret_city(city) for city in self.sta])

            if self.L[at] == 0:
                print("Visited at depth 0:", self.ret_city(at))
            else:
                print(f"Visited at depth {self.L[at]}:", [self.ret_city(city) for city in range(self.N) if self.L[city] == self.L[at]])
                
            self.path.pop()  # Remove the current node from path if it's not the goal
        return False

    def inc_limit(self):
        return not all(self.Acc)

    @staticmethod
    def ret_city(i):
        cities = ["Buraydah", "Unayzah", "AlZulfi", "Al-Badai", "Riyadh-Alkhabra", "AlRass",
                  "UmSedrah", "Shakra", "Al-Bukayriyah", "Sheehyah", "Dhalfa", "Mulida"]
        return cities[i] if 0 <= i < len(cities) else "Unknown"

def main():
    print("Choose a city to start with (its number): ")
    cities = ["Buraydah", "Unayzah", "AlZulfi", "Al-Badai", "Riyadh-Alkhabra", "AlRass",
              "UmSedrah", "Shakra", "Al-Bukayriyah", "Sheehyah", "Dhalfa", "Mulida"]
    for idx, city in enumerate(cities):
        print(f"{city} [{idx}]")
    
    city_choice = int(input("\nInput starting city number: "))
    goal = int(input("\nInput goal city number: "))
    
    if city_choice < 0 or city_choice >= 12:
        print("Invalid input, please restart the program.")
        return
    
    searcher = IDS(12, city_choice, goal)
    searcher.search()

if __name__ == "__main__":
    main()
