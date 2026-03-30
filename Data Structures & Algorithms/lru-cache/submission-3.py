class ListNode:
    def __init__(self, key=0,val=0, next=None, prev=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.map={}
        self.left=ListNode()
        self.right=ListNode()
        self.left.next=self.right
        self.right.prev=self.left
    
    def insert(self,node):
        node.next,node.prev=self.right,self.right.prev
        self.right.prev.next=node
        self.right.prev=node
    
    def remove(self,node):
        prev,nxt=node.prev, node.next
        prev.next=nxt
        nxt.prev=prev
    
    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        newNode=ListNode(key,value)
        self.map[key]=newNode
        self.insert(newNode)

        if len(self.map)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.map[lru.key]

        
