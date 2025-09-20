from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # store packets in FIFO order
        self.packet_set = set()  # to check duplicates (source, destination, timestamp)
        self.dest_map = defaultdict(list)  # destination -> sorted list of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet_key = (source, destination, timestamp)
        
        # Check duplicate
        if packet_key in self.packet_set:
            return False
        
        # Remove oldest packet if memory limit exceeded
        if len(self.queue) == self.memoryLimit:
            old_packet = self.queue.popleft()
            self.packet_set.remove(tuple(old_packet))
            old_dest = old_packet[1]
            old_timestamp = old_packet[2]
            self.dest_map[old_dest].pop(0)  # first timestamp corresponds to FIFO removal

        # Add new packet
        self.queue.append([source, destination, timestamp])
        self.packet_set.add(packet_key)
        self.dest_map[destination].append(timestamp)
        
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.packet_set.remove(tuple(packet))
        dest = packet[1]
        ts = packet[2]
        self.dest_map[dest].pop(0)
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_map[destination]
        # Since timestamps are sorted, we can use binary search
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left
