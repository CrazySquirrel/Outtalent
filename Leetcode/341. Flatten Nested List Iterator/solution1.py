# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def dfs(l: [NestedInteger]):
            for n in l:
                if n.isInteger():
                    yield n.getInteger(),
                else:
                    yield from dfs(n.getList())

        self.generator = dfs(nestedList)
        self.tmp = None

    def next(self) -> int:
        if self.tmp is not None:
            result = self.tmp
            self.tmp = None
            return result[0]

        return self.generator.__next__()

    def hasNext(self) -> bool:
        try:
            if self.tmp is None: self.tmp = self.generator.__next__()
            return self.tmp is not None
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
