

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        count = 0
        h = []
        intervals.sort()
        for interval in intervals:
            if not h or interval[0] < h[0]:
                count += 1
            else:
                heapq.heappop(h)
            heapq.heappush(h, interval[1])
        return count
        
        
        
        
        
        