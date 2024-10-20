class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    """This class provides an implementation of a stack."""
    def __init__(self):
        #TODO1: Implement this method:
        self.head = None
        pass

    def pop(self):
        """Should raise an IndexError: pop from empty stack Exception
           if the stack is empty, otherwise removes and returns the item
           from the top of the stack."""
        #TODO2: Implement this method:
        if(self.head == None):
            raise IndexError("pop from empty stack Exception")
        else:
            headData = self.head.data
            self.head = self.head.next
            return headData
            

    def push(self, item):
        """Adds the item to the top of the stack."""
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def is_empty(self):
        """Returns True if there are no items on the stack, False otherwise."""
        #TODO4: Implement this method:
        if self.head is None:
            return True
        else:
            return False

class Room:
    """A room has a name, a boolean to designate if it is has an escape, and a boolean visited
        attribute. It also has four references to other rooms it may have links to.
        A room may have 0 to 4 links to other rooms.""" 
    def __init__(self, name, is_esc=False, rm1=None, rm2=None, rm3=None, rm4=None):
        self.name = name
        self.room1 = rm1
        self.room2 = rm2
        self.room3 = rm3
        self.room4 = rm4
        self.is_escape=is_esc
        self.visited=False

    def get_neighbors_list(self):
        """Returns a list of the links this room has to other rooms, its 'neighbors'.
            The order should be room1, room2, room3, room4.
            Note that if a room link is None, it is not included in the list."""
        #TODO5: Implement this method:
        links = []
        if self.room1 is not None:
            links.append(self.room1)
        if self.room2 is not None:
            links.append(self.room2)
        if self.room3 is not None:
            links.append(self.room3)
        if self.room4 is not None:
            links.append(self.room4)
        return links

    def __str__(self):
        rm1str = '-'
        if self.room1:
            rm1str = self.room1.name
        rm2str = '-'
        if self.room2:
            rm2str = self.room2.name
        rm3str = '-'
        if self.room3:
            rm3str = self.room3.name
        rm4str = '-'
        if self.room4:
            rm4str = self.room4.name
        info_str = f'{"<"} {self.name} {"is esc:"}{self.is_escape} {"visited:"}{self.visited} ' \
        f'{"rm1:"}{rm1str} ' \
        f'{"rm2:"}{rm2str} ' \
        f'{"rm3:"}{rm3str} ' \
        f'{"rm4:"}{rm4str} {">"}' 
        return(info_str)

def find_escapes(start_room):
    """Uses a Stack instance to search the maze of rooms for the rooms that have 
    an escape: is_escape==True. Returns a list of the rooms designated as having an escape.
    This function also returns a list of the rooms in the order they were visited.
    Note: there may be more than one room with an escape, therefore the algorithm should
    visit every room in the maze and not stop when it finds an escape.
    See the instructions for more on this algorithm."""
    stack = Stack()
    esc_list = []
    visited_list = []
    #TODO6: Implement the rest of this method:
    stack.push(start_room)
    while stack.is_empty() is False:
        current_room = stack.pop()
        if current_room not in visited_list:
            visited_list.append(current_room)
            if current_room.is_escape == True:
                esc_list.append(current_room)
            else:
                neighbors = current_room.get_neighbors_list()
                for neighbor in neighbors:
                    stack.push(neighbor)
    return esc_list,visited_list
    

