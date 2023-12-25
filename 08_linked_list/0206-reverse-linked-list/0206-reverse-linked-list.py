class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
          return head

        cur = head
        prev = None

        while cur:
          nextone = cur.next
          cur.next = prev
          prev = cur
          cur = nextone

        return prev