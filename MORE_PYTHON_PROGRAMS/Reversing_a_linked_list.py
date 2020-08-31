class node:
        def __init__(self,data=None):
                self.data=data
                self.next=None

class linked_list:
        def __init__(self):
                self.head = None

##        ADD A NODE AT START:
        def push(self,data):
                new_node = node(data)
                new_node.next = self.head
                self.head = new_node

##        ADD A NODE AT LAST
        def append(self,data):
            new_node = node(data)
            cur_node = self.head

            if not cur_node:
                self.head = new_node
                return

            while cur_node:
                prev_node = cur_node
                cur_node = cur_node.next

            prev_node.next = node(data)

##        REVERSING A LINKED LIST
        def reverse(self):
            cur_node  = self.head
            prev_node = None
            while cur_node:
                next_node = cur_node.next
                cur_node.next = prev_node
                prev_node = cur_node
                cur_node = next_node

            self.head = prev_node 
                    

        def print_list(self):
                cur_node = self.head

                while cur_node:
                        print(cur_node.data,end = " ")
                        cur_node = cur_node.next
                        

l = linked_list()

l.push(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)


l.reverse()
l.print_list()

##
##def reverse(self):
##            cur_node  = self.head
##            
##            prev_node = None
##
##            while cur_node.next:
##                next_node = cur_node.next
##                cur_node.next = prev_node
##                prev_node = cur_node
##                cur_node = next_node
##
##            self.head = cur_node
##            self.head.next = prev_node
##


        
