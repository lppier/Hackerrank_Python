# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = nestedList
        self.inneriter = None
        self.cur = -1


    def next(self):
        """
        :rtype: int
        """
        if self.inneriter: 
            return self.inneriter.next()
        
        return self.data[self.cur].getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        # Takes care of case when we are in the inner list
        if self.inneriter and self.inneriter.hasNext():
            return True
        
        # If normal, or there is no more next item in the inner list
        self.inneriter = None # trick: "switch off the self inneriter" when no more need
        if self.cur < len(self.data) -1 : 
            self.cur += 1
            if self.data[self.cur].isInteger():
                return True
            # otherwise it's a list, and we recursively define a NestedIterator
            self.inneriter = NestedIterator(self.data[self.cur].getList())
            if self.inneriter.hasNext():
                return True
            self.inneriter = None
            return self.hasNext()
        return False
            
        


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())