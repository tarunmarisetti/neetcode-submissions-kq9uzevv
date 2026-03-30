class ListNode:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.left=ListNode(0,0)
        self.right=ListNode(0,0)
        self.left.next=self.right
        self.right.prev=self.left

        self.nodeMap={}
        self.capacity=capacity
        self.size=0

    def addAtEnd(self,node):
        prev=self.right.prev
        prev.next=node
        node.prev=prev
        node.next=self.right
        self.right.prev=node
    
    def removeFromBegin(self,node):
        curr=node
        prev=curr.prev
        prev.next=curr.next
        curr.next.prev=prev

    def get(self, key):
        if key in self.nodeMap:
            node=self.nodeMap[key]
            self.removeFromBegin(node)
            self.addAtEnd(node)
            return node.val
        return -1


    def put(self, key, val):
        # if key already present
        curr=None
        if key in self.nodeMap:
            curr=self.nodeMap[key]
        
        if curr:
            self.removeFromBegin(curr)
            curr.val=val
            self.addAtEnd(curr)
            return

        if self.size==self.capacity:
            frontNode=self.left.next
            self.removeFromBegin(frontNode)
            del self.nodeMap[frontNode.key]

            self.size-=1
        
        newNode=ListNode(key,val)
        self.nodeMap[key]=newNode
        self.size+=1
        self.addAtEnd(newNode)    
        
