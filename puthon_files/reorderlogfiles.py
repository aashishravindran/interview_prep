# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.
# ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]



# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

# letter=[]
# dig=[]
# for log in logs:
# 	_id,rest=log.split(" ",1)
# 	if rest[0].isalpha():
		
# 		letter.append(log)
# 	else:
# 		dig.append(log)
# 	print(_id,rest)

def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda key:key[0])
        
        prev=intervals[0]
        for interval in intervals:
        	if prev[1]>interval[1]:
        		return False
        	
        return True

print(canAttendMeetings())

[0,2,4,1,null,3,-1,5,1,null,6,null,8]