from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        l = len(beginWord)
        cd = defaultdict(list)
        for word in wordList:
            for i in range(l):
                cd[word[:i] + '*' + word[i+1:]].append(word)

        queue = [(beginWord, 1)]
        visited = {beginWord: True}

        while queue:
            c_word, level = queue.pop(0)
            for j in range(l):
                check_word = c_word[:j] + '*' + c_word[j+1:]
                for word in cd[check_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                cd[check_word] = []
        return 0

#can be also solved using bi-directional BFS to optimize it.
