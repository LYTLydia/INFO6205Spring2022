#Q1
import random
from heapq import merge


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur1=list1
        head=list2
        count=0
        while count<a-1:
            cur1=cur1.next
            count+=1

        cur2=cur1
        while count <b+1:
            cur2=cur2.next
            count+=1

        cur1.next=head

#find the tail of list2
        while head != None:
            head = head.next
            count+=1

        head.next=cur2

        return list1

#Q2
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p,q=ListNode(0),ListNode(0)
        p.next=head
        head1=p
        head2=q
        while p.next:
            if p.next.val<x:
                p=p.next
            else:
                q.next=p.next
                p.next=p.next.next
                q=q.next
                q.next=None

        p.next=head2.next
        return head1.next

#Q3
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next

        def reverse(m,n):
            while m<n:
                arr[m],arr[n]=arr[n],arr[m]
                m+=1
                n-=1 #reserve every element

        i,j,l=0,1,len(arr)
        while i<l:
            last=min(i+j,l)
            if (last-i)%2==0:
                reverse(i,last-1)
            i=last
            j+=1

        p=re_head=ListNode()
        for v in arr:
            p.next=ListNode(v)
            p=p.next

        return re_head.next

#Q4
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        abs=[]
        dis=[]
        if head == None:
            return [-1,-1]

        while head:
            arr.append(head.val)
            head=head.next

        for i in range(1,len(arr)-1):
            if(arr[i-1]<arr[i] and arr[i+1]<arr[i])or(arr[i]<arr[i-1] and arr[i]<arr[i+1]):
                abs.append(i)

        if len(abs)>2:
            for m in range(0,len(abs)-1):
                n=abs[m+1]-abs[m]
                dis.append(n)
                m+=1
            return [min(dis),abs[-1]-abs[0]]
        elif len(abs)==2:
            return [abs[-1]-abs[0],abs[-1]-abs[0]]
        else:
            return [-1,-1]

#Q5
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next

        arr.sort()

        p=re_head=ListNode
        for v in arr:
            p.next=ListNode(v)
            p=p.next
        return re_head.next

#Q6
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self. arr=[]
        while head:
            self.arr.append(head.val)
            head=head.next


    def getRandom(self) -> int:
        return random.choice(self.arr)

#Q7
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next

        arr[left-1:right]=list(reversed(arr[left-1:right]))

        p=re_head=ListNode
        for v in arr:
            p.next=ListNode(v)
            p=p.next

        return re_head.next
