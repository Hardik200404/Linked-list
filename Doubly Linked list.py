class Node:
    def __init__(self,n):
        self.info=n
        self.next=None
        self.prev=None

class l_list:
    def __init__(self):
        self.head=None
    
    def creating(self):
        size=int(input("Enter the size of your linked list: "))
        if size==0 or size<0:
            return None
        ch=input("Type 'front' to insert at front,and 'end',to insert at the back")
        while size>0:
            if ch=='front':
                n=int(input("Enter element: "))
                self.inserting_front(n)
            elif ch=='end':
                n=int(input("Enter element: "))
                self.inserting_end(n)
            else:
                print("Invalid input")
                break    
            size-=1
    def inserting_front(self,n):
        node=Node(n)
        #lets say user gave input in the order of 1,2,3,4
        #then then list should look like 4-3-2-1
        if self.head is None:#when creating the first node
            node.next=self.head
            self.head=node#now self.head is 1
        else:#when 2nd input is given ,i.e 2
            self.head.prev=node#1.prev=2
            node.next=self.head#2.next=1
            self.head=node#2 is now the head
        
    def inserting_end(self,n):
        node=Node(n)
        #lets say user gave input in the order of 1,2,3,4
        #then then list should look like 1-2-3-4
        if self.head is None:
            node.prev=self.head
            self.head=node
        else:
            #when 2nd input is given ,i.e 2
            temp=self.head#temp=1
            while temp.next is not None:#to get the last node, whose next will be none
                temp=temp.next
            temp.next=node#1.next=2
            node.prev=temp#2.prev=1
            temp=node#we are inserting at the end so,we wont update the self.head
                    
    def Display(self):
        ch=input("Type 'normal' to print normally,'backwards' to print backwards")
        temp=self.head
        if ch=='normal':
            while temp is not None:
                print(temp.info,end=" <-> ")
                temp=temp.next
        elif ch=='backwards':
            while temp is not None:
                if temp.next is None:
                    last=temp#acquiring last node
                temp=temp.next
            while last is not None:#traversing from the back
                print(last.info,end=" <-> ")
                last=last.prev
        else:
            print("Invalid entry")
                
    def delete(self,n):
        temp=self.head
        flag=False
        if self.head.info==n:#deleting head node
            temp1=temp.next
            temp1.prev=None
            temp.next=None
            self.head=temp1
            flag=True
        else:
            while temp is not None:
                if temp.info==n:
                    temp1=temp.prev#lets say l.list is 4-3-2-1,now temp1 will be 4,if n=3
                    temp1.next=temp.next#4.next=2
                    temp.next=None#3.next=None
                    temp1.next.prev=temp1#2.prev=4
                    temp.prev=None#3.prev=None
                    flag=True
                    break
                temp=temp.next

                #incase user wants to delete last node
                if temp.next is None:
                    if temp.info is n:
                        temp.prev.next=None
                        temp.prev=None
                        flag=True
                        break
                    else:
                        break
        if flag is True:
            print(n," has been deleted from your Linked list")
        else:
            print(n," doesn't exist in your Linked list")
            
    def insert_before(self,n):
        new_node=Node(n)
        node=int(input("Enter the node before which you want to insert"))
        flag=False
        temp=self.head
        if temp.info==node:#to insert before head node
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
            flag=True
        else:
            while temp is not None:
                #lets say the l.list is looking like 4-3-2-1
                #lets say user wants to insert 5 before 3
                if temp.next.info == node:#4.next,i.e 3==3 true
                    temp.next.prev=new_node#3.prev=5
                    new_node.next=temp.next#5.next=3
                    temp.next=new_node#4.next=5
                    new_node.prev=temp#5.prev=4
                    flag=True
                    break
                temp=temp.next
                if temp.next is None:
                    if temp.info!=node:#incase compiler reached the end and given node doesn't exist
                        break
                
        if flag is True:
            print(f"{n} has been inserted before {node}") 
        else:
            print(f"{node} doesn't exist in your Linked list")
        
    def insert_after(self,n):
        new_node=Node(n)
        flag=False
        node=int(input("Enter the node after which you want to insert"))
        temp=self.head
        while temp is not None:
            if temp.info==node:
                temp.next.prev=new_node
                new_node.next=temp.next
                new_node.prev=temp
                temp.next=new_node
                flag=True
                break
            temp=temp.next
            if temp.next is None:
                if temp.info == node:#to insert after last node
                    temp.next=new_node
                    new_node.prev=temp
                    flag=True
                    break
                else:
                    break
        if flag is True:
            print(f"{n} has been inserted after {node}")
        else:
            print(f"{node} doesn't exist in your Linked list")
            
    def search(self):
        temp=self.head
        count=0
        node=int(input("Enter the node which you want to search"))
        flag=False
        while temp is not None:
            if temp.info is node:
                print(f"{node} is in index {count}")
                flag=True
            count+=1
            temp=temp.next
        if flag is False:
            print(f"{node} doesn't exist in your Linked list")
            
    def replace(self):
        n=int(input("Enter new node"))
        new_node=Node(n)
        node=int(input("Enter the node which you want to replace"))
        temp=self.head
        flag=False
        if self.head.info==node:#l.list is 4-3-2-1,temp is 4 
            new_node.next=temp.next#for example 5 is the new node,5.next is 3
            temp.next.prev=new_node#3.prev is 5
            temp.next=None
            self.head=new_node
            flag=True
        else:
            while temp is not None:
                if temp.info == node:#lets say user wants to replace 3 with 5
                    new_node.next=temp.next#5.next is 2
                    temp.next.prev=new_node#2.prev is 5
                    temp.next=None#3.next is None
                    temp.prev.next=new_node#4.next is 5
                    new_node.prev=temp.prev#5.prev is 4
                    temp.prev=None#3.prev is none
                    flag=True
                    break
                temp=temp.next
                if temp.next is None:#incase compiler reached last node
                    #lets say l.list is looking like 4-3-2-1
                    if temp.info ==node:#incase 5 is new node
                        temp.prev.next=new_node#2.next is 5
                        new_node.prev=temp.prev#5.prev is 2
                        temp.prev=None#1.prev=none
                        flag=True
                        break
                    else:#incase compiler reached end but given node was not the last node
                        break
        if flag is True:
            print(f"{node} has been replaced by {n}")
        else:
            print(node," doesn't exist in your Linked list")
            
obj=l_list()
obj.creating()
print("1:Display")
print("2:Insert")
print("3:Delete")
print("4:Replace")
print("5:Search")
print("Type 'stop'/'end'/'exit' to exit!!")
while True:
    print()
    ch=input("Enter choice: ")
    if ch=='stop' or ch=='end' or ch=='exit':
        break
    elif ch=='1':
        obj.Display()
    elif ch=='2':
        ch=input("\nType 'before' to insert before an element,and 'after' for after an element: ")
        if ch=='before':
            n=int(input("\nEnter the new element: "))
            obj.insert_before(n)
        elif ch=='after':
            n=int(input("\nEnter the new element: "))
            obj.insert_after(n)
        else:
            print("Inavlid entry")
    elif ch=='3':
        n=int(input("\nEnter the element you want to delete: "))
        obj.delete(n)
    elif ch=='4':
        obj.replace()
    elif ch=='5':
        obj.search()
    else:
        print("Invalid entry")