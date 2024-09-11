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

    
    while len(search_queue) > 0 :
        next_state = search_queue.get()
        if goal_test :
            return next_state
        else: 
            edges = next_state.mars_graph.getEdges(start_state)
            ##queue 
            for e in edges :
                ##
                search_queue.put(next_state.g + heuristic_fn(e), next_state.mars_graph.getNode())


    ## you do the rest.


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

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
        files = f.readlines()
        
        g = Graph(len(files))
        for line in files :
            #ex: elements  = ['1,1:', '2,1', '1,2']
            elements = line.strip("\n").split(" ")

            print(elements)
            #ex: src = '1,1'
            src = elements[0].rstrip(":")
            n = Node(src)
            #Node added sucessfully!
            g.add_node(n)
            for dest in elements[1:]: 
                print("EDGES: " + dest)
                #e = ('1,1', '1,2')
                e = Edge(n, dest)

                g.add_edge(e)
                        
        #return the graph
        
        return g
  

if __name__ == '__main__':
    x = "1, 2"
    read_mars_graph("MarsMap")
