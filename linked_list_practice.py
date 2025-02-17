class ListNode:

    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next

#creating individual nodes
node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(1)
node4 = ListNode(10)
node5= ListNode(3)

#Linking the Nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#Assigning the Head of the Node
head = node1

#Traversing the List
current = head
while current:
    print(current.val)
    current = current.next
print("None")

#Removing duplicates
l=set()
current = head
previous = None
while current:
    if current.val not in l:
        l.add(current.val)
        previous= current
    else:
        previous.next = current.next
    current=current.next

print(head)

#Reversing a Linked List
current = head
previous=None
while current:
    nextnode = current.next
    current.next = previous
    previous = current
    current = nextnode

print(previous)

#Merging two sorted lists
list1=[1,2,4]
list2=[1,3,4]
one_list=[]
a=list1
b=list2
while a and b:
    if a.val < b.val:
        one_list.append(a.val)
        a=a.next
    else:
        one_list.append(b.val)
        b=b.next
while a:
    one_list.append(a.val)
    a=a.next

while b:
    one_list.append(b.val)
    b=b.next

if not one_list:
    print None
previous = ListNode()
head = previous
for i in one_list:
    current = listNode(i)
    previous.next = current
    previous = current
return head.next








