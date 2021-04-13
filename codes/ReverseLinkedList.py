# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        start=head
        previous=None
        start_next=None
        while (start!=None):
            start_next=start.next
            start.next=previous
            previous=start
            start=start_next
        return previous
head=ListNode(1)
t=head
for i in range(2,6):
    t.next=ListNode(i)
    t=t.next
a=Solution()
head=a.reverseList(head)
while head!=None:
    print head.val
    head=head.next
