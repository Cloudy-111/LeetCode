from queue import Queue
import bisect


class Router:

    def __init__(self, memoryLimit: int):
        self.queue = Queue()
        self.limit = memoryLimit
        self.packet = {}
        self.map_des = {}
        self.des_nums_out = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.packet:
            return False

        if destination not in self.map_des:
            self.map_des[destination] = []
            self.map_des[destination].append(timestamp)
        else:
            self.map_des[destination].append(timestamp)

        self.queue.put([source, destination, timestamp])
        if self.queue.qsize() > self.limit:
            source_out, des_out, timestamp_out = self.queue.get()
            self.des_nums_out[des_out] += 1
            del self.packet[(source_out, des_out, timestamp_out)]
        self.packet[(source, destination, timestamp)] = 1
        return True

    def forwardPacket(self) -> List[int]:
        if self.queue.qsize() == 0:
            return []

        source, destination, timestamp = self.queue.get()
        del self.packet[(source, destination, timestamp)]
        self.des_nums_out[destination] += 1
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.map_des:
            return 0
        arr = self.map_des[destination]
        start_offset = self.des_nums_out[destination]

        if start_offset >= len(arr):
            return 0

        if startTime > arr[-1] or endTime < arr[start_offset]:
            return 0

        start_index = bisect.bisect_left(arr, startTime, lo=start_offset)
        end_index = bisect.bisect_right(arr, endTime, lo=start_offset)

        return end_index - start_index


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
