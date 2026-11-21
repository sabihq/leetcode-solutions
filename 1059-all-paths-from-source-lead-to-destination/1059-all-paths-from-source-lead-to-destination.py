class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)

        state = [0] * n

        def dfs(node):
            if not graph[node]:
                return node == destination

            if state[node] == 1:
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2
            return True

        return dfs(source)