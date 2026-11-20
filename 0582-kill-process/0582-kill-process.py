from collections import defaultdict, deque
from typing import List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = defaultdict(list)

        # Step 1: Build parent-to-children mapping
        for i in range(len(pid)):
            children[ppid[i]].append(pid[i])

        # Step 2: BFS to find all processes to kill
        result = []
        queue = deque([kill])

        while queue:
            process = queue.popleft()
            result.append(process)

            for child in children[process]:
                queue.append(child)

        return result