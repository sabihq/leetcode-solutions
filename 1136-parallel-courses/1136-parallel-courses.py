from collections import deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)

        for prev, next_course in relations:
            graph[prev].append(next_course)
            indegree[next_course] += 1

        queue = deque()

        for course in range(1, n + 1):
            if indegree[course] == 0:
                queue.append(course)

        semesters = 0
        completed = 0

        while queue:
            semesters += 1

            for _ in range(len(queue)):
                course = queue.popleft()
                completed += 1

                for next_course in graph[course]:
                    indegree[next_course] -= 1

                    if indegree[next_course] == 0:
                        queue.append(next_course)

        return semesters if completed == n else -1