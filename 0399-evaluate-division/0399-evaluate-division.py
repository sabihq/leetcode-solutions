class Solution(object):
    def calcEquation(self, equations, values, queries):
        # Build a weighted graph
        graph = {}

        for i in range(len(equations)):
            numerator, denominator = equations[i]
            value = values[i]

            if numerator not in graph:
                graph[numerator] = []
            if denominator not in graph:
                graph[denominator] = []

            # numerator / denominator = value
            graph[numerator].append((denominator, value))

            # denominator / numerator = 1 / value
            graph[denominator].append((numerator, 1.0 / value))

        def dfs(current, target, product, visited):
            if current == target:
                return product

            visited.add(current)

            for neighbor, value in graph[current]:
                if neighbor not in visited:
                    answer = dfs(
                        neighbor,
                        target,
                        product * value,
                        visited
                    )

                    if answer != -1.0:
                        return answer

            return -1.0

        answers = []

        for numerator, denominator in queries:
            # Either variable is undefined
            if numerator not in graph or denominator not in graph:
                answers.append(-1.0)
            else:
                answers.append(
                    dfs(numerator, denominator, 1.0, set())
                )

        return answers