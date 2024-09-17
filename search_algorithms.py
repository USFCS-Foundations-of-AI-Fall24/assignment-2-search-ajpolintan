from collections import deque

## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    states = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                print("Previous")
                ptr = ptr.prev
                print(ptr)
            print("----------------------")
            print("Breath First Search")
            print("STATES: " + str(states))
            print("----------------------")

            return next_state
        else :
            successors = next_state[0].successors(action_list)
            states = states + len(successors)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=0) :
    search_queue = deque()
    closed_list = {}
    states = 0


    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                print("Previous")
                ptr = ptr.prev
                print(ptr)
            print("----------------------")
            print("Depth First Search")
            print("STATES: " + str(states))
            print("----------------------")

            return next_state
        else :
            successors = next_state[0].successors(action_list)
            states = states + len(successors)

            #increment every thing in s list by 1
            depth = 0
            for item in successors :
                item[0].depth = depth
                depth = depth + 1

            #filter the items if item.depth is greater than the limit 
            if (limit != 0) :
                successors = [item for item in successors if item[0].depth < limit]
                
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            depth = depth + 1
            search_queue.extend(successors)

def depth_limited_search(startState, action_list, goal_test, limit, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    states = 0

    #limit variable in the state
    #increment limit. Do not increment every time you call limit 
    #Create a variable called depth in the state class
    #Increase depth member variable to state class by one everytime you increase 
    #After you called sucessors from depth first search, Only enqueue the things that are less than the limit

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)

            print("----------------------")
            print("Depth Limited Search")
            print("STATES: " + str(states))
            print("----------------------")

            return next_state
        else :
            successors = next_state[0].successors(action_list)
            states = states + len(successors)

            depth = 0
            for item in successors :
                item[0].depth = depth
                depth = depth + 1
            
            if limit != 0 :
                successors = [item for item in successors if item[0].depth < limit]

            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True

            search_queue.extend(successors)
    print("STATE NOT FOUND IN DEPTH LIMITED SEARCH")
## add iterative deepening search here