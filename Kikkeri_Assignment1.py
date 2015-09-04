#Pradyumna Kikkeri, CSCI 3202, 101417122 Student ID

import random
import Queue

# Python implementation of a queue of 10 integers, part a in assignment 1

q = Queue.Queue() #initialiaze the Queue module

print "\n"
print "10 random integers in the queue, dequeued, are:"

x = random.sample(range(1, 500), 10) #generates 10 integers in the range of 1-500 using the random module

q.put(x) #put the 10 generated integers into the queue

print q.get() #dequeue and print the integers in the order in which they were dequeued
print "\n"

####################################################################################################################

#Stack implementation

class Stack:
     def __init__(self):
         self.items = [] #Initializing list object

     def isEmpty(self):
         return self.items == [] #check if stack is empty

     def push(self, item):
         self.items.append(item) #push item onto the stack

     def pop(self):
         return self.items.pop() #pop top of stack off, thus, FIFO

     def size(self):
         return len(self.items) #size of stack, unused


s = Stack()

print "Is stack currently empty? True or false?"
print(s.isEmpty())
print "\n"


#I came up with 10 random integers in my head and brute-force pushed them onto the stack
print "Pushing 10 integers onto stack, they are 5, 2, 52, 13, 22, 456, 23, 67, 11, 29, in that order. Stack is LIFO, so when popping, 29 should come first, followed by the others...\n"
s.push(5)
s.push(2)
s.push(52)
s.push(13)
s.push(22)
s.push(456)
s.push(23)
s.push(67)
s.push(11)
s.push(29)

#Now, we are popping the stack, top element first, so the numbers above should be printed in reverse order.
print "Popping stack - Success! Results shown below."

print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()

print "\n"
print "Onto the tree."

##################################################################################################################################

# Binary tree implementation
# Node first

class Node:
    def __init__(self, intkey):
        self.key = intkey
        self.childleft = None
        self.childright = None
        self.parent_key = None


# Now the actual tree

class Tree:
    def __init__(self, intkey):
        self.key = intkey
        self.childleft = None
        self.childright = None
        self.parent_key = None

    def delete(self, intkey, parentNode):
        if parentNode is None:
            print "That node wasn't found."
            return False
        elif intkey == parentNode.key:
            if parentNode.childleft or parentNode.childright:
                print "Node not deleted, has children."
                return False
            else:
                del parentNode.childleft
                del parentNode.childright
                del parentNode.parent_key
                del parentNode.key
                del parentNode
                return True
        elif intkey < parentNode.key:
            self.delete(intkey, parentNode.childleft)
        else:
            try:
                self.delete(intkey, parentNode.childright)
            except:
                pass




def add(parentValue, value):
    if parentValue is None:
        print "Parent not found."
    if (parentValue.childright and parentValue.childleft):
        print "Parent has two children, node not added."
    else:
        if parentValue.key > value.key:
            if parentValue.childleft == None:
                    parentValue.childleft = value
                    value.parent_key = parentValue
            else:
                    add(parentValue.childleft, value)
        else:
            if parentValue.childright == None:
                parentValue.childright = value
                value.parent_key = parentValue
            else:
                add(parentValue.childright, value)

def tree_print(parentNode):
    if not parentNode:
        return
    try:
        print parentNode.key
    except:
        pass
    try:
        tree_print(parentNode.childleft)
    except:
        pass
    try:
        tree_print(parentNode.childright)
    except:
        pass

print "Adding integers 6-15 in order\n"
binary_tree = Tree(6)
add(binary_tree, Node(7))
add(binary_tree, Node(8))
add(binary_tree, Node(9))
add(binary_tree, Node(10))
add(binary_tree, Node(11))
add(binary_tree, Node(12))
add(binary_tree, Node(13))
add(binary_tree, Node(14))
add(binary_tree, Node(15))

print "The preorder traversal is:\n"

tree_print(binary_tree)

print "\n"

print "Now attempting to delete 2 integers."

binary_tree.delete(15, binary_tree)
binary_tree.delete(12, binary_tree)

tree_print(binary_tree)

#################################################################################################################################

#Graph implemenation


class UnweightedGraph():
    def __init__(self):
        self.vertex_list = {}

    def addVertex(self, value):
        if(value in self.vertex_list):
            print "Vertex already exists!"
        else:
            self.vertex_list[value] = []
        return

    def addEdge(self, value1, value2):
        if (not value1 in self.vertex_list or not value2 in self.vertex_list):
            print 'One or more vertex/vertices not found.'
        else:
            self.vertex_list[value1].append(value2)
            self.vertex_list[value2].append(value1)
        return

    def findVertex(self, value):
        if (not value in self.vertex_list):
            print "That vertex doesn't exist."
        else:
            print str(value) + " has an adjacency list -- i.e. has edges to vertex keys --" + ' ' + str(self.vertex_list[value])
        return

print "\nNow testing graph. Adding edges 1-10."

g = UnweightedGraph()

for i in range(1,11):
    g.addVertex(i)

print "\nSuccess!"

print "\nTesting adding an existing vertex, vertex 3."

g.addVertex(3)
print "\n"

print "Now adding 20 edges to the graph."

g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 9)
g.addEdge(3, 6)
g.addEdge(3, 9)
g.addEdge(4, 8)
g.addEdge(4, 6)
g.addEdge(6, 8)
g.addEdge(9, 2)
g.addEdge(10, 1)
g.addEdge(10, 2)
g.addEdge(10, 3)
g.addEdge(7, 1)
g.addEdge(7, 5)
g.addEdge(7, 3)
g.addEdge(8, 3)

print "\nSuccess! Now going to test adding between non existent vertices '12' and '15'"

g.addEdge(12, 1)
g.addEdge(1, 15)

print "\n"
print "Now going to find adjacency lists for 5 vertices: 3, 6, 7, 1, 10\n"

g.findVertex(3)
g.findVertex(6)
g.findVertex(7)
g.findVertex(1)
g.findVertex(10)

print "\nNow going to try to find for a nonexisting vertex '20'."

g.findVertex(20)

print "\nAssignment 1 complete!\n"