#Q1
# Definition for singly-linked list.
import heapq


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

#Q3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTowLists(self, l1, l2):
        head=dummy=ListNode()
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                dummy.next=l1
                l1=l1.next
            else:
                dummy.next=l2
                l2=l2.next
            dummy=dummy.next
        if l1==None:
            dummy.next=l2
        else:
            dummy.next=l1
        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lens=len(lists)
        if lens==0:
            return None
        elif lens==1:
            return lists[0]
        else:
            half=lens//2
            return self.mergeTowLists(self.mergeKLists(lists[:half]),self.mergeKLists(lists[half:]))

#Q4
class Solution:
    def reorderList(self, head: ListNode) -> None:
        length, first = 0, head
        while first:
            length += 1
            first = first.next
        left = length // 2

        l_list, node, cur = [], head, 0
        while cur < length:
            if cur > left:
                l_list.append(node)
            node = node.next
            cur += 1
        ans = node = head

        for i in range(len(l_list) - 1, -1, -1):
            new = l_list[i]
            temp = node.next
            node.next = new
            new.next = temp
            node = node.next.next

        if length % 2 == 0:
            node.next.next = None
        else:
            node.next = None

#Q5
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev,rev.next,slow = slow,rev,slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

#Q6
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a = head
        b = head

        for i in range(n):
            if a.next:
                a = a.next
            else:
                return head.next

        while a.next:
            a = a.next
            b = b.next
        b.next = b.next.next
        return head


#Q7
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd, even = head, head.next
        cp_even = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = cp_even

        return head


#Q8
class Solution:
    def insert(self,head:'Node',insertVal:int)->'Node':
        if head == None:
            node=Node(insertVal)
            node.next=node
            return node

        cur=head
        while cur.next.val>=cur.val and cur.next!=head:
            cur=cur.next

        first=cur.next
        last=cur
        node=Node(insertVal)
        if first.val>=insertVal:
            node.next=first
            last.next=node
            return head

        cur=first
        while cur.next.val<insertVal:
            cur=cur.next

        node.next=cur.next
        cur.next=node
        return head


#Q9
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []
        if not head.next:
            return [0]

        res=[]
        while head:
            res.append(head.val)
            head=head.next

        stack=[]
        for index,value in enumerate(res):
            if index==0:
                stack.append((index,value))
            while stack and value>stack[-1][1]:
                res[stack[-1][0]]=value
                stack.pop()
            stack.append((index,value))

        if stack:
            for i in stack:
                res[i[0]]=0

        return res


#Q10
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        dummy=ListNode(0,head)

        cur=dummy
        while cur.next and cur.next.next:
            if cur.next.val==cur.next.next.val:
                temp=cur.next.val
                while cur.next and cur.next.val==temp:
                    cur.next=cur.next.next
            else:
                cur=cur.next

        return dummy.next