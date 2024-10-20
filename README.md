**Maze Search Project**

**Overview**
This project implements a maze search algorithm using a stack-based approach. It demonstrates the use of depth-first search (DFS) for solving mazes. The primary data structure used is a stack, which allows backtracking when dead ends are encountered in the maze.

**Features**
Stack Implementation: A custom stack data structure is implemented from scratch using a linked list approach. The stack provides essential operations such as push, pop, and is_empty.

Maze Search Algorithm: The depth-first search (DFS) algorithm is utilized to navigate through the maze, leveraging the stack for exploring possible paths and backtracking when necessary.

**Project Structure**
Node Class: Defines individual elements in the stack.

Stack Class: Implements a stack using a linked list structure. Supports the following methods:

push(item): Adds an item to the top of the stack.

pop(): Removes and returns the item from the top of the stack. Raises an IndexError if the stack is empty.

is_empty(): Returns True if the stack is empty, otherwise returns False.

**How to Run**
Clone or Download: Download the project and ensure you have Python installed on your system.

Execute the Python Script: Run the maze_search.py script to see how the stack-based maze search algorithm works.

bash
Copy code
python maze_search.py
Modify the Maze: You can modify the maze structure in the script to test different configurations and see how the search algorithm handles them.

**Dependencies**
This project does not have any external dependencies and runs on any standard Python environment (Python 3.x).

**License**
This project is open-source and can be freely modified and distributed.
