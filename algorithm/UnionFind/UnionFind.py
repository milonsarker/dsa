class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    def printRoot(self):
        for idx, val in enumerate(self.root):
            print(str(val) + '___' + str(idx) + '   ', end = '' )
        print()
    def find(self, x):
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
if __name__=="__main__":
    uf = UnionFind(10)
    #uf.printRoot()
    print("1-2-5-6-7 3-8-9 4")
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    uf.printRoot()
    print(uf.isConnected(1, 5))  # true
    print(uf.isConnected(5, 7))  # true
    print(uf.isConnected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.isConnected(4, 9))  # true