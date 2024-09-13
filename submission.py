from mars_planner import *
from routefinder import *

if __name__ == '__main__' :


    s1 = RoverState()
    result1 = breadth_first_search(s1, action_list, mission_complete)
    result1 = depth_first_search(s1, action_list, mission_complete)
    result1 = depth_limited_search(s1, action_list, mission_complete,10)


    s2 = RoverState()
    print(s2)
    result2 = breadth_first_search(s2, action_list, moveToSampleGoal)
    result3 = breadth_first_search(result2[0], action_list, removeSampleGoal)
    result4 = breadth_first_search(result3[0], action_list, returnToChargerGoal)

    s1 = map_state(g=1,h=1,location="8,8")
    result = a_star(s1, sld, reachedGoal)
    result = a_star(s1, h1, reachedGoal)