#Linkedlist Operations
'''
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        self.head=Node(data,self.head)
    def insert_at_ending(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_ending(data)
    def print(self):
        if self.head is None:
            print("Linked list is empty")
        itr=self.head
        lstr=""
        while itr:
            lstr+=str(itr.data)+"==>"
            itr=itr.next
        print(lstr)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        if index==0:
            return self.insert_at_beginning(data)
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=Node(data,itr.next)
                break
            itr=itr.next
            count+=1
l1=Linkedlist()
l1.insert_at_beginning(5)
l1.insert_at_beginning(54)
l1.insert_at_beginning(60)
l1.insert_at_ending(50)
l1.insert_at_ending(59)
l1.print()
print("Length of the linkedlist is :",l1.get_length())
l1.insert_values(['a','b','c','d','e','f','g'])
l1.print()
print("Length of the linkedlist is :",l1.get_length())
l1.remove_at(2)
l1.print()
#l1.remove_at(20) --->Exception case
l1.insert_at(2,"likky")
l1.insert_at(0,"anu")
l1.insert_at(6,"vinee")
l1.print()
'''
#Reverse the linkedlist
'''
class Node(object):
    def __init__(self,val,next):
        self.val=val
        self.next=next
class ListNode:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_values(self,data_list):
        for i in data_list:
            self.insert_at_end(i)
    def reverse_linkedlist(self):
        prev=None
        itr=self.head
        while itr:
            nxt=itr.next
            itr.next=prev
            prev=itr
            itr=nxt
        return prev
l1=ListNode()
l1.insert_values([1,2,3,4,5])
print(l1.reverse_linkedlist())
'''

#Middle of the linkedlist
'''
def middle_linkedlist(head):
    fast,slow=head,head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow

def middle_linkedlist(head):
    c=0
    itr=head
    while itr:
        itr=itr.next
        c+=1
    t=0
    itr=head
    while itr:
        if t>=(c//2):
            return itr
        itr=itr.next
        t+=1
'''

#Merge sorted linkedlist
'''
def merge_linkedlist(l1,l2):
    head=ListNode()
    itr=head
    while l1 and l2:
        if l1.val>l2.val:
            itr.next=l2
            l2=l2.next
        else:
            itr.next=l1
            l1=l1.next
        itr=itr.next
    while l1:
        itr.next=l1
        itr=itr.next
        l1=l1.next
    while l2:
        itr.next=l2
        itr=itr.next
        l2=l2.next
    return head.next
'''
#Palindrome linkedlist
'''
def palindrome_linkedlist(head):
    fast,slow=head,head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    prev=None
    while slow:
        nxt=slow.next
        slow.next=prev
        prev=slow
        slow=nxt
    left,right=head,prev
    while right:
        if left.val!=right.val:
            return False
        left=left.next
        right=right.next
    return True

def palindrome_linkedlist(head):
    l=[]
    while head:
        l.append(head.val):
        head=head.next
    return l==l[::-1]
'''
#detect cycle
'''
def detect_cycle(head):
    fast,slow=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False2
'''
#Add two numbers
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head=ListNode()
        itr=head
        temp=0
        while l1 or l2 or temp:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            a=v1+v2+temp
            temp=a//10
            itr.next=ListNode(a%10)
            itr=itr.next
            if l1:l1=l1.next 
            if l2:l2=l2.next 
        return head.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head=ListNode()
        itr=head
        temp=0
        while l1 and l2:
            a=l1.val+l2.val+temp
            if len(str(a))!=1:
                itr.next=ListNode(a%10)
                temp=a//10
            else:
                itr.next=ListNode(l1.val+l2.val+temp)
                temp=0
            itr=itr.next
            l1=l1.next
            l2=l2.next
        while l1:
            a=l1.val+temp
            if len(str(a))!=1:
                itr.next=ListNode(a%10)
                temp=a//10
            else:
                itr.next=ListNode(l1.val+temp)
                temp=0
            itr=itr.next
            l1=l1.next
        while l2:
            a=l2.val+temp
            if len(str(a))!=1:
                itr.next=ListNode(a%10)
                temp=a//10
            else:
                itr.next=ListNode(l2.val+temp)
                temp=0
            itr=itr.next
            l2=l2.next
        if temp:
            itr.next=ListNode(temp)
        return head.next
'''



