from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        head_list = []
        now = head
        while True:
            head_list.append(now.val)
            if now.next != None: 
                now = now.next
                continue
            break

        if head_list == head_list[::-1]:
            return True
        else:
            return False