# Given the root of a binary tree, return the level order traversal 
# of its node's value (from left to right, level by level)

# Pattern 
# We want to use a breadth first search on the tree and then add the values to a list 
# Then we can use a Queue (FIFO) algorithm to hold our values added

# class Solution: 
#     def levelOrder(self, root:optional[TreeNode]) -> List([List[int]]):
        
        # First we want to initialize the variables 
        result = []
        # initialize a queue 
        q = collections.deque() 
        q.append(root) # make sure to first append the root

        while q: 
            qlength = len(q)
            level = []

            for i in range(qlength):
                  node = q.popleft()

                  if node: 
                    level.append(node.val) # remember we want the value as stated in the problem 
                    q.append(node.left)# we need to add the left to right first 
                    q.append(node.right)


            if level: 
                result.append(level)

        return result
            
# Summary we start at the root node when we start our queue
# while the queue is not empty we want to start at a new level sublist and we want to get the length of the queue
# keep in mind the queue will be changing as we are popping and adding elements to it 
# for i in the queue, we want to pop/ remove the  value as the node. if the node exists then we want to append that node's VALUE to the level's sublist
# NOW for the node's children we need to append them to the queue
# now we want to append the level we gone through to the result.
# keep in mind the result will be a list of sublists of levels