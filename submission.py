from mars_planner import *
from routefinder import *

if __name__ == '__main__' :

    #MARS PLANNER TESTS
    s1 = RoverState()
    result1 = breadth_first_search(s1, action_list, mission_complete)
    result1 = depth_first_search(s1, action_list, mission_complete)
    result1 = depth_limited_search(s1, action_list, mission_complete,10)


    s2 = RoverState()
    print(s2)
    result2 = breadth_first_search(s2, action_list, moveToSampleGoal)
    result3 = breadth_first_search(result2[0], action_list, removeSampleGoal)
    result4 = breadth_first_search(result3[0], action_list, returnToChargerGoal)

    #ROVER FINDER TESTS
    s1 = map_state(g=1,h=1,location="8,8")
    result = a_star(s1, sld, reachedGoal)
    result = a_star(s1, h1, reachedGoal)
    print("---------------")
    s2 = map_state(g=1,h=1,location="4,4")
    result = a_star(s2, sld, reachedGoal)
    result = a_star(s2, h1, reachedGoal)
    print("---------------")
    s3 = map_state(g=1,h=1,location="3,6")
    result = a_star(s3, sld, reachedGoal)
    result = a_star(s3, h1, reachedGoal)
    print("---------------")
    s4 = map_state(g=1,h=1,location="1,4")
    result = a_star(s4, sld, reachedGoal)
    result = a_star(s4, h1, reachedGoal)
    print("---------------")

    #Run mapcoloring.py in terminal by using python mapcoloring.py 