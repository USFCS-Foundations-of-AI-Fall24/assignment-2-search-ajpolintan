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
    states = 0
    
    # add starting state to closed list. CLOSED LIST IS A LIST OF STATES. NEEDS TO BE EDGES OR NODES
    if use_closed_list : 
        closed_list[start_state] = True

    # while the priority queue is not full
    while search_queue.qsize() > 0 :
        next_state = search_queue.get()
        print("NEXT STATE: " + str(next_state))
        graph = next_state.mars_graph
        #If the goal is found
        if goal_test(next_state) :
            print("YOU REACHED THE GOAL!")
            print("TOTAL STATES: " + str(states))
            return next_state
        else: 
            #get edges must use a node. How do I get the next_states node 
            currentNode = Node(next_state.location)
            print(graph.get_edges(next_state.location))
            
            edges = next_state.mars_graph.get_edges(next_state.location)
            #sucessfully got the edges
            print("---------")
            print(edges)
            print("---------")

            #GENERATE SUCCESSORS
            successors = [] 
            #Check neighbors and add neighbors to sucesssors list. This appends the EDGES
            for e in edges :
                #create map states for every edge. Check if map state is already present
                m = map_state(g=1, h=0, location=e.dest)
                #UPDATE HEURISTIC
                m.h = heuristic_fn(m)
                #UPDATE TOTAL ESTIMATED COST
                m.f = m.g + m.h
                successors.append(m)

                #Added cost
                #g will always be 1 because you are always move one forward SUCESSORS IS A LIST OF EDGES
            states = states + len(successors)
            print(states)
            if use_closed_list :
                #filter if there is a similar state
                successors = [item for item in successors
                                    if item not in closed_list]
                for s in successors :
                    closed_list[s] = True

            for m in successors:
                search_queue.put(m, m.f)




    ## you do the rest.



## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)

def sld(state) :
   #idea -> get location (1,1)
   #split -> split data point into x and y 
   loc = str(state.location).split(",")
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

         #   print(elements)
            #ex: src = '1,1'
            src = elements[0].rstrip(":")
            n = Node(src)
            #Node added sucessfully!
            g.add_node(n.value)
            for dest in elements[1:]: 
               # print("EDGES: " + dest)
                #e = ('1,1', '1,2')
                e = Edge(src, dest)
                g.add_edge(e)
                        
        #return the graph
        
        return g
  
def reachedGoal(s) :
    return s.location == "1,1"

if __name__ == '__main__':
    x = "1, 2"
    s1 = map_state(g=1,h=1,location="1,3")
    result = a_star(s1, sld, reachedGoal)
    read_mars_graph("MarsMap")
