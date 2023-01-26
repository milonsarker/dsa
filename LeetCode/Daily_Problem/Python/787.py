#https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict, deque
import heapq
from typing import List

## Dijkstra
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        visited = {}
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        pq = [(0, 0, src)]
        while pq:
            cost, stops, node = heapq.heappop(pq)
            if node == dst and stops - 1 <= k:
                return cost
            if node not in visited or visited[node] > stops:
                visited[node] = stops
                for neighbor, price in adj[node]:
                    heapq.heappush(pq, (cost + price, stops + 1, neighbor))
        return -1


## BFS solution
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        queue = deque()
        queue.append((src, 0))
        costs = [float("inf")] * n
        while queue and k >= 0:
            m = len(queue)
            for _ in range(m):
                curr, cost = queue.popleft()
                for node, price in adj[curr]:
                    if cost + price < costs[node]:
                        costs[node] = cost + price
                        queue.append((node, costs[node]))
            k -= 1
        return costs[dst] if costs[dst] != float("inf") else -1


## Bellman Ford
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        costs = [float("inf")] * n

        costs[src] = 0
        for i in range(k + 1):
            temp = costs.copy()
            for start, end, price in flights:
                if costs[start] != float("inf"):
                    temp[end] = min(costs[start] + price, temp[end])
            costs = temp
        return costs[dst] if costs[dst] != float("inf") else -1