class ListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None

class MyHashMap:

    def __init__(self):
        self.size=1000
        self.memory=[None]*self.size
        

    def put(self, key: int, value: int) -> None:
        hashCode=key%self.size
        curr=self.memory[hashCode]
        if not curr:
            self.memory[hashCode]=ListNode(key,value)
            return
        while curr:
            if curr.key==key:
                curr.val=value
                return
            elif not curr.next:
                curr.next=ListNode(key,value)
                return
            curr=curr.next
        

    def get(self, key: int) -> int:
        hashCode=key%self.size
        curr=self.memory[hashCode]
        if not curr:
            return -1
        while curr:
            if curr.key==key:
                return curr.val
            curr=curr.next
        return -1 
        

    def remove(self, key: int) -> None:
        hashCode=key%self.size
        curr=self.memory[hashCode]
        if not curr:
            return
        prev=None
        while curr:
            if curr.key==key:
                if prev:
                    prev.next=curr.next
                else:
                    self.memory[hashCode]=curr.next
                return
            prev=curr
            curr=curr.next
        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)