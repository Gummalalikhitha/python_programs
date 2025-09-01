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

            
        
        
