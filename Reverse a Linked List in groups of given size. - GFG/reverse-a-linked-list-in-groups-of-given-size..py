"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        # Code here
        def reverse(root):
            prev = None
            curr = root
            while curr:
                _next = curr.next
                curr.next = prev
                prev = curr
                curr = _next
            root_1 = prev
            
            return root_1, root 
        
        curr = head
        for i in range(k-1):
            if curr.next:
                curr = curr.next
            else: break
        _next = curr.next
        curr.next = None
        start_1, end_1 = reverse(head)
        # head_1 = head
        head = _next
        # return root_1
        while head:
            curr = head
            for i in range(k-1):
                if curr.next:
                    curr = curr.next
                else: break
            _next = curr.next
            curr.next = None
            start, end = reverse(head)
            end_1.next = start
            end_1 = end
            head = _next
        return start_1
            


#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends