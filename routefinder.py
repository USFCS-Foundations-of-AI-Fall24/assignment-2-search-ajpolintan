from queue import PriorityQueue
from math import sqrt
from Graph import Graph,Node,Edge
class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = read_mars_graph("MarsMap")
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put(start_state)
    ## you do the rest.


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    state.location = "1,1"
    return 

## you do this - return the straight-line distance between the state and (1,1)

def sld(state) :
   #idea -> get location (1,1)
   #split -> split data point into x and y 
   loc = state.location.split(",")
   return sqrt(((int(loc[0]) - 1) ** 2) + ((int(loc[1]) - 1) ** 2))

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    with open(filename) as f:   
        files = f.readLines()
        
        g = Graph(len(files))
        
        for line in f.readlines() :
            elements = line.strip("\n").split(" ")
            n = Node(elements[0].rstrip[":"])
            g.add_node(n)
            if len(line) > 0 :
                print(line)

if __name__ == '__main__':
    x = "1, 2"
    read_mars_graph("MarsMap")
