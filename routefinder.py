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
    
    # Add starting map state to closed list 
    if use_closed_list : 
        closed_list[start_state] = True

    # Look until search queue is full
    while search_queue.qsize() > 0 :
        # Get the next state and graph in the queue
        next_state = search_queue.get()
        graph = next_state.mars_graph
        print("NEXT STATE: " + str(next_state))

        #If the goal is found
        #If the state passes the goal test 
        if goal_test(next_state) :
            print("YOU REACHED THE GOAL!")
            print("TOTAL STATES: " + str(states))
            return next_state
        else: 
            #get the edges from the curren mars_graph         
            edges = graph.get_edges(next_state.location)
           
            #sucessfully got the edges
            print("---------")
            print(edges)
            print("---------")

            #Gain successsors (The edges that are not added yet)
            successors = [] 
            #Loop through edges and add to successors list
            for e in edges :
                #Create a map state for every edge
                m = map_state(g=1, h=0, location=e.dest)
                #Update Heuristic and total cost
                m.h = heuristic_fn(m)
                m.f = m.g + m.h

                #add the state to successors
                successors.append(m)

            #Calculate number of states
            states = states + len(successors)
            print(states)

            #Filter out any states present in the closest list in successors
            if use_closed_list :
                #filter if there is a similar state
                successors = [item for item in successors
                                    if item not in closed_list]
                #Add any remaining successors to closed list
                for s in successors :
                    closed_list[s] = True
            #Put map states in the queue
            for m in successors:
                search_queue.put(m, m.f)




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
  
# goal functions
def reachedGoal(s) :
    return s.location == "1,1"

if __name__ == '__main__':
    s1 = map_state(g=1,h=1,location="8,8")
    result = a_star(s1, sld, reachedGoal)
    result = a_star(s1, h1, reachedGoal)

    read_mars_graph("MarsMap")
