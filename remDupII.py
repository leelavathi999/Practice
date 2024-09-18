class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def removeDuplicates(self,head:ListNode)->ListNode:
        dummy=ListNode(0,head)
        prev=dummy
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                prev.next=head.next
            else:
                prev=prev.next
            head=head.next
        return dummy.next


def listToLinkedlist(arr):
    if not arr:
        return None
    head=ListNode(arr[0])
    current=head
    for value in arr[1:]:
        current.next=ListNode(value)
        current=current.next
    return head


def linkedlistToList(head):
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    return result


arr=[1,2,3,3,4,4,5]
head=listToLinkedlist(arr)

output=Solution().removeDuplicates(head)
listOutput=linkedlistToList(output)
print(listOutput)