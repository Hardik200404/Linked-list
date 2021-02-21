class Node:
    def __init__(self,n):
        self.info=n
        self.next=None
class l_list:
    def __init__(self):
        self.head=None
    
    def creating(self):
        size=int(input("Enter the size of your linked list: "))
        if size==0 or size<0:
            return None
        ch=input("Type 'front' to insert at front,and 'end',to insert at the back: ")
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
        node.next=self.head
        self.head=node#every time a new element is added,it becomes the head.
        
    def inserting_end(self,n):
        node=Node(n)
        if self.head is None:#for the first element
            self.head=node
            return#important to return
        
        temp=self.head
        while temp.next is not None:#this loop is used to reach the element who next is none
            temp=temp.next
        temp.next=node
            
    def Display(self):
        temp=self.head
        if temp is None:
            print("Linked list is empty")
            return None
        while temp is not None:
            print(temp.info,end="-->")
            temp=temp.next
            
    def delete(self,n):
        temp=self.head
        flag=False
        if temp.info==n:#incase the given number is the head node
            self.head=temp.next
            temp.next=None
            flag=True
        else:
            while temp is not None:
                #for example l.list is 1->2->3->4->,and user wants to delete 3
                #so when 2.next==3 true
                if temp.next.info==n:
                    temp1=temp.next#temp1=3
                    temp.next=temp.next.next#2.next=4
                    temp1.next=None#3.next=none
                    flag=True
                    break
                temp=temp.next
        if flag is True:
            print(n,"has been deleted")
        else:
            print(n,"was not found in the Linked list")
            
    def insert_before(self,n):
        temp=self.head
        flag=False
        new_node=Node(n)#Creating a new node for the new element
        node=int(input("Enter the node/element before which you want to insert: "))
        if temp.info==node:#incase user wants to insert the element before the head
            self.head=new_node
            new_node.next=temp
            flag=True
        
        else:
            while temp is not None:
                if temp.next.info==node:
                    new_node.next=temp.next
                    temp.next=new_node
                    flag=True
                    break
                temp=temp.next
                if temp.next is None:#incase the element is not there,and the complier reached towards the end
                    break
        
        if flag==True:
            print(n,"has been inserted before,",node)
        else:
            print("Given node doesn't exist in your Linked list")
            
    def insert_after(self,n):
        temp=self.head
        flag=False
        node=int(input("Enter the node after which you want to insert"))
        new_node=Node(n)#Creating a new node for the new element
        if temp.info==node:#for after head node
            new_node.next=temp.next
            temp.next=new_node
            flag=True
        else:
            while temp is not None:
                if temp.next.info == node:
                    temp=temp.next
                    new_node.next=temp.next
                    temp.next=new_node
                    flag=True
                    break
                temp=temp.next
                if temp.next is None:#incase the element is not there,and the complier reached towards the end
                    break
        if flag==True:
            print(n,"has been inserted after,",node)
        else:
            print("Given node doesn't exist in your Linked lsit")
            
    def search(self):
        count=0
        temp=self.head
        num=int(input("Enter the element you want to search: "))
        flag=False
        while temp is not None:
            if temp.info==num:
               print(num,f"is in index :{count}")
               flag=True
            temp=temp.next
            count+=1
        if flag==False:
            print(num,"is not present in the list")
            
    def replace(self):
        temp=self.head
        flag=False
        num=int(input("Enter the new element: "))
        new_node=Node(num)
        node=int(input("Enter the node/element which you want to replace: "))
        if self.head.info==node:#incase the given node is the head node 
            self.head=new_node
            self.head.next=temp.next
            flag=True
        while temp is not None:
            #for example l.list is 1->2->3->4->,and user wants to replace 3 with 5
            #so when 2.next==3 true
            if temp.next.info==node:
                temp1=temp.next#temp1=3
                new_node.next=temp.next.next#5.next=2.next.next,i.e 4
                temp.next=new_node#2.next=5
                temp1.next=None
                flag=True
                break
            temp=temp.next
            if temp.next is None:#incase the element is not there,and the complier reached towards the end
                    break
        if flag==True:
            print(f"{node} has been replaced by {num}")
        else:
            print(f"{node} not found in your Linked list")
            
obj=l_list()
obj.creating()
print()
print("1:Display")
print("2:Insert")
print("3:Delete")
print("4:Replace")
print("5:Search")
print("Type 'stop'/'end'/'exit' to exit!!")
while True:
    print()
    ch=input("Enter your choice: ")
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
        n=int(input("\nEnter the element you want to delete"))
        obj.delete(n)
    elif ch=='4':
        obj.replace()
    elif ch=='5':
        obj.search()
    else:
        print("Invalid entry")