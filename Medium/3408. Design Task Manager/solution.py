class TaskManager:

    heap = []
    map_task = {}
    user_task = {}
    remove_task = {}

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.map_task = {}
        self.user_task = {}
        self.remove_task = {}
        heapq.heapify(self.heap)
        for task in tasks:
            heapq.heappush(self.heap, [-task[2], -task[1], task[0]])
            if task[1] not in self.map_task:
                self.map_task[task[1]] = task[2]
            if task[1] not in self.user_task:
                self.user_task[task[1]] = task[0]

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, [-priority, -taskId, userId])
        self.user_task[taskId] = userId
        self.map_task[taskId] = priority
        if taskId in self.remove_task:
            del self.remove_task[taskId]

    def edit(self, taskId: int, newPriority: int) -> None:
        self.map_task[taskId] = newPriority
        heapq.heappush(self.heap, [-newPriority, -
                       taskId, self.user_task[taskId]])
        if taskId in self.remove_task:
            del self.remove_task[taskId]

    def rmv(self, taskId: int) -> None:
        self.remove_task[taskId] = True

    def execTop(self) -> int:
        while self.heap and (
            self.remove_task.get(-self.heap[0][1], False)
            or self.heap[0][2] != self.user_task.get(-self.heap[0][1], None)
            or -self.heap[0][0] != self.map_task.get(-self.heap[0][1], None)
        ):
            heapq.heappop(self.heap)

        if len(self.heap) == 0:
            return -1

        priority, neg_taskId, userId = heapq.heappop(self.heap)
        taskId = -neg_taskId

        if taskId in self.map_task:
            del self.map_task[taskId]
        if taskId in self.user_task:
            del self.user_task[taskId]
        if taskId in self.remove_task:
            del self.remove_task[taskId]

        return userId


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
