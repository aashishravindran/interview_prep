"""
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.

"""
def isOneEditDistance(a,b):
	#  if a and b differe by a length >1 then return False 
	if a==" " and b==" ":
		return False
	if abs(len(a)-len(b))>1:
		return False 
	# lets get two vectors shorter and longer 
	shorter,longer=sorted([a,b],key=len)
	for i in range(len(shorter)):
		if shorter[i] != longer[i]:
			# if the strings are not equal the we have two cases 
			# the case where the strings are of the same length  
			# in which case i expect all characters except the curr one to bet the same 
			if len(shorter)==len(longer):
				return shorter[i+1:]==longer[i+1:]
			# or i expect the longer string to differ by atmost one character

			else:
				return shorter[i:]==longer[i+1:]
	#  and edge case might be they may differ by one hcaracter in the end, 
	# so we can just insert that character and check inf length are equla 
	return len(shorter)+1 == len(longer)
s = "cab"
t = "ad"
print(isOneEditDistance(s,t))