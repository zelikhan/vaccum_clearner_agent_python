# we have to achieve this goal state
goalstate = {'A': '0', 'B': '0', 'C': '0', 'D': '0'}
action = 0
cost = 0  # it will measure the cost
roomstate = {'A': '0', 'B': '0', 'C': '0', 'D': '0'}  # current state is 0
print("Enter starting location:")
location = input()
for room in roomstate:
    action = input("Enter the state of {} room ". format(room))
    roomstate[room] = action
print("Vaccun placed in location {} ".format(location))
if (goalstate != roomstate):
    if(roomstate['A'] == '1'):
        roomstate['A'] = '0'
        print("Room A is CLeaned")
        cost = cost+1
    if(goalstate == roomstate):
        print("Goal State has been met")
        print("Cost : {}".format(str(cost)))

    else:
        print("Room A is clean ")
        print("Moving to room B ")
        cost = cost+1
    if(roomstate['B'] == '1'):
        roomstate['B'] = '0'
        print("Room B is CLeaned")
        cost = cost+1

    if(goalstate == roomstate):
        print("Goal State has been met")
        print("Cost : {}".format(str(cost)))

    else:
        print("Room is already clean")
        print("Moving to room B ")
        cost = cost+1
    if(roomstate['C'] == '1'):
        roomstate['C'] = '0'
        print("Room C is CLeaned")
        cost = cost+1

    if(goalstate == roomstate):
        print("Goal State has been met")
        print("Cost : {}".format(str(cost)))

    else:
        print("Room C is already clean")
        print("Moving to room D ")
        cost = cost+1
    if(roomstate['D'] == '1'):
        roomstate['D'] = '0'
        print("Room D is CLeaned")
        cost = cost+1

    if(goalstate == roomstate):
        print("Goal State has been met")
        print("Cost : {}".format(str(cost)))

    else:
        print("Room D is already clean")
