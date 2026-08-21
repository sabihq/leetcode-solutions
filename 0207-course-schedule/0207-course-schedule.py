class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # adjacency[course] contains courses unlocked by completing it
        adjacency = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            adjacency[prerequisite].append(course)
            indegree[course] += 1

        # Begin with courses that have no prerequisites
        queue = []

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed = 0
        front = 0

        while front < len(queue):
            course = queue[front]
            front += 1
            completed += 1

            # Completing this course removes it as a prerequisite
            for next_course in adjacency[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses