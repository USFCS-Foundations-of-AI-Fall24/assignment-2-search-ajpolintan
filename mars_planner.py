## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search,depth_first_search,depth_limited_search

class RoverState :
    
    def __init__(self, loc="station", sample_extracted=False, holding_sample=False, holding_tool=False, charged=False, depth=0):
        self.loc = loc
        self.sample_extracted=sample_extracted
        self.holding_sample = holding_sample
        self.holding_tool = holding_tool
        self.charged = charged
        self.prev = None
        self.depth = 0
     
#slist = s1.successors
#for item in slist
    #item.depth += s1.depth + 1
    ## you do this.
    def __eq__(self, other):
       return (self.loc == other.loc and 
              self.sample_extracted == other.sample_extracted
              and self.holding_sample == other.holding_sample
              and self.holding_tool == other.holding_tool
              and self.charged == other.charged)


    def __repr__(self):
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n"+
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Holding Tool? : {self.holding_tool}\n" +
                f"Charged? {self.charged}")

    def __hash__(self):
        return self.__repr__().__hash__()

    def successors(self, list_of_actions):

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also

        ##explanation to myself. list of actions are applied. Self is the current state. Each action is applied to the state. If the state is the same the item is removed  
        succ = [(item(self), item.__name__) for item in list_of_actions]

        depth = 0
        for item in succ :
            item[0].depth = depth
            depth = depth + 1
        ## remove actions that have no effect
        succ = [item for item in succ if not item[0] == self]

        return succ

## our actions will be functions that return a new state.

def move_to_sample(state) :
    r2 = deepcopy(state)
    r2.loc = "sample"
    r2.prev = state
    return r2
def move_to_station(state) :
    r2 = deepcopy(state)
    r2.loc = "station"
    r2.prev = state
    return r2

def move_to_battery(state) :
    r2 = deepcopy(state)
    r2.loc = "battery"
    r2.prev = state
    return r2
# add tool functions here

def pick_up_tool(state) :
    r2 = deepcopy(state)
    r2.holding_tool = True
    r2.prev = state
    return r2

def drop_tool(state) :
    r2 = deepcopy(state)
    r2.holding_tool = False
    r2.prev = state
    return r2

def use_tool(state) :
    r2 = deepcopy(state)
    r2.sample_extracted = True
    r2.prev = state
    return r2

def pick_up_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.holding_sample = True
    r2.prev = state
    return r2

def drop_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "station":
        r2.holding_sample = False
    r2.prev = state
    return r2

def charge(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.charged = True
    r2.prev = state
    return r2


action_list = [charge, drop_sample, pick_up_sample,
               move_to_sample, move_to_battery, move_to_station, pick_up_tool, drop_tool,
               use_tool]

## goal functions
def battery_goal(state) :
    return state.loc == "battery"
def sample_goal(state) :
    return state.loc == "sample" and state.sample_extracted == True
def station_goal(state) :
    return state.loc == "station"

def moveToSampleGoal(s):
    return s.loc == "sample"
def removeSampleGoal(s):
    return s.sample_extracted == True 
def returnToChargerGoal(s):
    return s.loc == "battery" and s.charged == True


## add your goals here.

def mission_complete(state) :
    return state.charged == True and state.loc == "battery" and state.sample_extracted == True
    
if __name__=="__main__" :

    def g(s):
            return s.loc == "battery" and s.sample_extracted == True and s.charged == True
            
    def moveToSampleTest(s):
        return s.loc == "sample" 
    def removeSampleTest(s):
        return s.sample_extracted == True 
    def returnToChargerTest(s):
        return s.loc == "battery" and s.charged == True
    


    s1 = RoverState()
    result1 = breadth_first_search(s1, action_list, mission_complete)
    result1 = depth_first_search(s1, action_list, mission_complete)
    result1 = depth_limited_search(s1, action_list, mission_complete,10)


    s2 = RoverState()
    print(s2)
    result2 = breadth_first_search(s2, action_list, moveToSampleTest)
    result3 = breadth_first_search(result2[0], action_list, removeSampleTest)
    result4 = breadth_first_search(result3[0], action_list, returnToChargerTest)

    #print(result2)
    #45 if you do problem decomposition vs 61 if you do not do problem decompositon 
    #result = breadth_first_search(s, action_list, battery_goal)

  



