# https://leetcode.com/problems/word-ladder/
# 123.Word Ladder

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import collections 
        def getTransformations(wordList):
            transformations=collections.defaultdict(list)
            
            for word in wordList:
                for i in range(len(word)):
                    t_word=word[0:i]+"*"+word[i+1:len(word)]
                    transformations[t_word].append(word)
            
            return transformations
        
        
        
        allTrans=getTransformations(wordList)
        queue=collections.deque()
        queue.append((beginWord,1))
        visited=set()
        visited.add(beginWord)
        
        while queue:
            word,distance=queue.popleft()
            for i in range(len(word)):
                trans=word[0:i]+"*"+word[i+1:len(word)]
                canReach=allTrans.get(trans,[])
                
                for reachable in canReach:
                    if reachable == endWord:
                        return distance+1
                    if reachable not in visited:
                        visited.add(reachable)
                        queue.append((reachable,distance+1))
        return 0
