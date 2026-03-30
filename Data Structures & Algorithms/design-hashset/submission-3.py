class ListNode:
    def __init__(self,key):
        self.key=key
        self.next=None

class MyHashSet:

    def __init__(self):
        self.size=1000
        self.memory=[None]*self.size
        

    def add(self, key: int) -> None:
        hashCode=key%self.size
        curr=self.memory[hashCode]
        if curr:
            while curr:
                if curr.key==key:
                    return
                elif not curr.next:
                    curr.next=ListNode(key)
                    return
                curr=curr.next
        elif not curr:
            self.memory[hashCode]=ListNode(key)
            return


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
        

    def contains(self, key: int) -> bool:
        hashCode=key%self.size
        curr=self.memory[hashCode]
        while curr:
            if curr.key==key:
                return True
            curr=curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)