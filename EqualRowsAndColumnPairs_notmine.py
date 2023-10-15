class eqpairs(object):
    def equalPairs(self, grid):
        lookup = {}
        for i, row in enumerate(grid):
            lookup[tuple(row)] = lookup.get(tuple(row), 0) + 1
            print(row[2])
        ans = 0
        for j in range(len(grid)):
            ans += lookup.get(tuple(row[j] for row in grid), 0)
            print(j, tuple(row[j] for row in grid),0)
        return ans


print(eqpairs().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))