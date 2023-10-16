
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        current = self.head
        if not self.head:
           return -1
        
        while(current.next and index > 0):
            current = current.next
            index -= 1
        if(index > 0):
            return -1
        else:
            return current.data

            

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """

        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        if not self.head:
            return
        current = self.head
        while(current.next and index > 1):
            current = current.next
            index -= 1
        if(index == 1):
            new_node.next = current.next
            current.next = new_node        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if not self.head:
            return
        current = self.head
        if(index == 0):
            self.head = current.next
            return
        while(current.next and current.next.next and index > 1):
            current = current.next
            index -= 1
        if(index == 1 and current.):
            current.next = current.next.next


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)