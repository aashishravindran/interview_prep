# Merge Intervals

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda key: key[0])
        
        merged_val=[]
        
        for interval in intervals:
            if len(merged_val)==0:
                merged_val.append(interval)
            else:
                previous_interval=merged_val[len(merged_val)-1]
                if previous_interval[1]<interval[0]:
                    merged_val.append(interval)
                else:
                    previous_interval[1]=max(previous_interval[1],interval[1])
        return merged_val