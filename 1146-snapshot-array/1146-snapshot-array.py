class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        records = self.history[index]

        if records[-1][0] == self.snap_id:
            records[-1] = (self.snap_id, val)
        else:
            records.append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        records = self.history[index]
        left, right = 0, len(records) - 1

        while left <= right:
            mid = (left + right) // 2

            if records[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return records[right][1]