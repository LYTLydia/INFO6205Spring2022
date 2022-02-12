#Q1
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total=0
        nextCarry=0
        result=ListNode()
        cur=result
        while l1!=None and l2!=None:
            total=l1.val+l2.val+nextCarry
            cur.next=ListNode(total%10)
            nextCarry=total//10
            l1=l1.next
            l2=l2.next
            cur=cur.next
        while l1!=None:
            total=l1.val+nextCarry
            cur.next=ListNode(total%10)
            nextCarry=total//10
            l1=l1.next
            cur=cur.next
        while l2!=None:
            total=l2.val+nextCarry
            cur.next=ListNode(total%10)
            nextCarry=total//10
            l2=l2.next
            cur=cur.next
        if nextCarry!=0:
            cur.next=ListNode(nextCarry)
        return result.next


#Q2

#Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def __init__(self):
        self.__dict__={}


    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def copy(cur:Node)->Node:
            if cur==None:
                return None
            elif cur in self.__dict__:
                return self.__dict__[cur]
            else:
                new_cur=Node(cur.val,None,None)
                self.__dict__[cur]=new_cur
                return self.__dict__[cur]

        cur=head
        new_head=copy(cur)
        new_cur=new_head

        while cur:
            new_cur.next=copy(cur.next)
            new_cur.random=copy(cur.random)
            new_cur=new_cur.next
            cur=cur.next

        return new_head
