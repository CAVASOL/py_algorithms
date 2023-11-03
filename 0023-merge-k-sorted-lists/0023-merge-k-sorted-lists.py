# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists):
        heap = PriorityQueue()
        for i, head in enumerate(lists):
            if head:
                heap.put((head.val, i))
        
        dummy = ListNode(0)
        curr = dummy

        while not heap.empty():
            val, i = heap.get()
            node = lists[i]
            curr.next = node
            curr = node
            if node.next:
                heap.put((node.next.val, i))
                lists[i] = node.next

        return dummy.next