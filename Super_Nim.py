state = ("min", 2, 4, 2, 3, 0, 0)


def succ(state):
    state1 = tuple()
    if state[0] == "min":
        state1 = state1 + ("max",)
        print state1
    elif state[0] == "max":
         state1 = state1 + ("min",)
         print state1


succ(state)
print len(state)

tup1 = ("min", 2, 4, 2, 3, 0, 0)
x = int(input("Press 1 to choose random player or 2 to choose AI player: \n"))

if x == 1:
    print"The game starts...."
    print(tup1[0] + " Turn")
    print(tup1[1:5])
    print("min score: "+str(tup1[5]))
    print("max score: "+str(tup1[6]))
    print("Press the corresponding number for selecting the move. All possible moves are shown below:")
    print("1: Place first heap on the second.\n2: Place first heap on the last.\n3: Place second heap on the last.")
    print("4: Cash-in on the first or third heap.")
    print("5: Split the second heap.")
    print("6; Apply Ulam step on the last one. (i.e. n --> 3n+1)\n")
    choice1 = int(input("Select 1-6: "))

    if choice1 == 1:
       tup2 = ("max", 6, 2, 3, 0, 0)
       print(tup2[0] + " Turn")
       print(tup2[1:4])
       print("min score: " + str(tup2[4]))
       print("max score: " + str(tup2[5]))
       print("Press the corresponding number for selecting the move. All possible moves are shown below:")
       print("1: Place first heap on the second.\n2: Place first heap on the last.\n3: Place second heap on the last.")
       print("4: Cash-in on the second heap.")
       print("5: Split the first heap.")
       print("6; Apply Ulam step on the last one. (i.e. n --> 3n+1)\n")
       choice2 = int(input("Select 1-6: "))


       if choice2 == 1:
           tup3 = ("min", 8, 3, 0, 0)
           print(tup3[0] + " Turn")
           print(tup3[1:3])
           print("min score: " + str(tup3[3]))
           print("max score: " + str(tup3[4]))
           print("Press the corresponding number for selecting the move. All possible moves are shown below:")
           print("1: Place first heap on the second.")
           print("2: Split the first heap.")
           print("3; Apply Ulam step on the last one. (i.e. n --> 3n+1)\n")
           choice3 = int(input("Select 1-3: "))
           if choice3 == 1:
               tup4 = ("max", 10, 0, 0)
               print(tup4[0] + " Turn")
               print(tup4[1:2])
               print("min score: " + str(tup4[2]))
               print("max score: " + str(tup4[3]))
               print("Press the corresponding number for selecting the move. All possible moves are shown below:")
               print("1: Place first heap on the second.")
               print("2: Split the first heap.")
               print("3; Apply Ulam step on the second heap. (i.e. n --> 3n+1)\n")
               choice4 = int(input("Select 1-3: "))
           if choice3 == 2:
               tup4 = ("max", 4, 4, 3, 0, 0)
               print(tup4[0] + " Turn")
               print(tup4[1:4])
               print("min score: " + str(tup4[4]))
               print("max score: " + str(tup4[5]))
               print("Press the corresponding number for selecting the move. All possible moves are shown below:")
               print("1: Place first heap on the second.")
               print("2: Split the first heap.")
               print("3; Apply Ulam step on the second heap. (i.e. n --> 3n+1)\n")
               choice4 = int(input("Select 1-3: "))
           if choice3 == 3:
               tup4 = ("max", 8, 10, 0, 0)
               print(tup4[0] + " Turn")
               print(tup4[1:3])
               print("min score: " + str(tup4[3]))
               print("max score: " + str(tup4[4]))
               print("Press the corresponding number for selecting the move. All possible moves are shown below:")
               print("1: Place first heap on the second.")
               print("2: Split the first heap.")
               print("3; Apply Ulam step on the second heap. (i.e. n --> 3n+1)\n")
               choice4 = int(input("Select 1-3: "))
       if choice2 == 2:
           tup3 = ("min", 2, 9, 0, 0)
           print(tup3[0] + " Turn")
           print(tup3[1:3])
           print("min score: " + str(tup3[3]))
           print("max score: " + str(tup3[4]))
           print("Press the corresponding number for selecting the move. All possible moves are shown below:")
           print("1: Place first heap on the second.")
           print("2: Cash-in on the first heap.")
           print("3; Apply Ulam step on the second heap. (i.e. n --> 3n+1)\n")
           choice3 = int(input("Select 1-3: "))
       if choice2 == 3:
           tup3 = ("min", 6, 5, 0, 0)
           print(tup3[0] + " Turn")
           print(tup3[1:3])
           print("min score: " + str(tup3[3]))
           print("max score: " + str(tup3[4]))
           print("Press the corresponding number for selecting the move. All possible moves are shown below:")
           print("1: Place first heap on the second.")
           print("2: Split the first heap.")
           print("3; Apply Ulam step on the second heap. (i.e. n --> 3n+1)\n")
           choice3 = int(input("Select 1-3: "))

       if choice2 == 4:
           tup3 = ("min", 6, 3, 2, 0)
           print(tup3[0] + " Turn")
           print(tup3[1:3])
           print("min score: " + str(tup3[3]))
           print("max score: " + str(tup3[4]))
           print("Press the corresponding number for selecting the move. All possible moves are shown below:")
           print("1: Place first heap on the second.")
           print("2: Split the first heap.")
           print("3; Apply Ulam step on the second heap. (i.e. n --> 3n+1)\n")
           choice3 = int(input("Select 1-3: "))
       if choice2 == 5:
           tup3 = ("min", 3, 3, 2, 3, 0, 0)
           print(tup3[0] + " Turn")
           print(tup3[1:5])
           print("min score: " + str(tup3[5]))
           print("max score: " + str(tup3[6 ]))
           print("Press the corresponding number for selecting the move. All possible moves are shown below:")
           print("1: Place first heap on the third.")
           print("2: Cash in on third heap.")
           print("3; Apply Ulam step on the first heap. (i.e. n --> 3n+1)\n")
           choice3 = int(input("Select 1-3: "))
       if choice2 == 6:
           tup3 = ("min", 6, 2, 10, 0, 0)
           print(tup3[0] + " Turn")
           print(tup3[1:4])
           print("min score: " + str(tup3[4]))
           print("max score: " + str(tup3[5]))
           print("Press the corresponding number for selecting the move. All possible moves are shown below:")
           print("1: Place first heap on the second.\n2: Place first heap on the third.\n3: Place second heap on the third.")
           print("4: Split the first heap.")
           print("5: Cash in in the second heap.")
           print("6: Split the third heap.")
           choice3 = int(input("Select 1-6: "))
    elif choice1 == 2:
       tup2 = ("max", 4, 2, 5, 0, 0)
       print(tup2[0] + " Turn")
       print(tup2[1:4])
       print("min score: " + str(tup2[4]))
       print("max score: " + str(tup2[5]))
    elif choice1 == 3:
       tup2 = ("max", 2, 4, 5, 0, 0)
       print(tup2[0] + " Turn")
       print(tup2[1:4])
       print("min score: " + str(tup2[4]))
       print("max score: " + str(tup2[5]))
    elif choice1 == 4:
       tup2 = ("max", 2, 4, 3, 0, 2)
       print(tup2[0] + " Turn")
       print(tup2[1:4])
       print("min score: " + str(tup2[4]))
       print("max score: " + str(tup2[5]))
    elif choice1 == 5:
       tup2 = ("max", 2, 2, 2, 2, 3, 0, 0)
       print(tup2[0] + " Turn")
       print(tup2[1:6])
       print("min score: " + str(tup2[6]))
       print("max score: " + str(tup2[7]))
    elif choice1 == 6:
       tup2 = ("max", 2, 4, 2, 10, 0, 0)
       print(tup2[0] + " Turn")
       print(tup2[1:5])
       print("min score: " + str(tup2[5]))
       print("max score: " + str(tup2[6]))

state = ("min", 2, 4, 0, 0)

class Super_Nim:

    def terminal(self, state):
        if len(state) == 3:
            return True
        else:
            return False

    def U_terminal(self, state):

            max_score = state[len(state)-2]
            min_score = state[len(state)-1]
            print "Score of max: ", max_score
            print "Score of min: ", min_score
            if max_score > min_score:
                print("Max won the game.")
            elif min_score > max_score:
                print("Min won the game.")
            else:
                print("The game is draw.")


    def player(self, state):
        return state[0]

    def succ(self, state):
        list_states = []
        for i in range(1, len(state) - 2):
            for j in range(1, len(state) - 2):
                state1 = tuple()
                if state[0] == "min":
                    state1 = state1 + ("max",)

                elif state[0] == "max":
                    state1 = state1 + ("min",)

                if i != j:
                    if state[i] != state[j]:
                        a = state[i] + state[j]
                        state1 = state1 + (a,)
                        for k in range(1, len(state)):
                            if k != i and k != j:
                                b = state[k]
                                state1 = state1 + (b,)
                        list_states.append(state1)
        for i in range(1, len(state) - 2):
            if state[i] % 2 == 0:
                if state[i] == 2:
                    state2 = tuple()
                    if state[0] == "min":
                        state2 = state2 + ("max",)

                    elif state[0] == "max":
                        state2 = state2 + ("min",)

                    for k in range(1, len(state)):
                        if k != i and k < len(state) - 2:
                            b = state[k]
                            state2 = state2 + (b,)
                        if k == len(state) - 2:
                            if state[0] == "min":
                                b = state[k]
                                state2 = state2 + (b,)
                            elif state[0] == "max":
                                b = state[k] + 2
                                state2 = state2 + (b,)
                        if k == len(state) - 1:
                            if state[0] == "min":
                                b = state[k] + 2
                                state2 = state2 + (b,)
                            elif state[0] == "max":
                                b = state[k]
                                state2 = state2 + (b,)

                    list_states.append(state2)
                else:
                    state3 = tuple()
                    if state[0] == "min":
                        state3 = state3 + ("max",)

                    elif state[0] == "max":
                        state3 = state3 + ("min",)
                    for k in range(1, len(state)):
                        if k == i:
                            b = state[k] / 2
                            state3 = state3 + (b,)
                            state3 = state3 + (b,)
                        else:
                            b = state[k]
                            state3 = state3 + (b,)
                    list_states.append(state3)
            else:
                state4 = tuple()
                if state[0] == "min":
                    state4 = state4 + ("max",)

                elif state[0] == "max":
                    state4 = state4 + ("min",)
                for k in range(1, len(state)):
                    if k == i:
                        b = 3 * state[k] + 1
                        state4 = state4 + (b,)

                    else:
                        b = state[k]
                        state4 = state4 + (b,)
                list_states.append(state4)
        # Removing duplicate states in the list
        final_list_states = []
        for element in list_states:
            if element not in final_list_states:
                final_list_states.append(element)
        return final_list_states

    def instruction(self, state):
        print(state[0] + " Turn")
        print(state[1:len(state) - 2])
        print("max score: " + str(state[len(state) - 2]))
        print("min score: " + str(state[len(state) - 1]))

    def random_move(self, list_states):

        move_select = input("Select your move from above list. Enter 1 for first, 2 for second and so on.\n")
        move = list_states[move_select-1]
        del list_states
        print move
        return move


nim = Super_Nim()

# player = nim.player(state)

# val = nim.succ(state)

for i in range(50):
    a = nim.terminal(state)
    if a is True:
        nim.U_terminal(state)
        break

    else:
        nim.instruction(state)
        list_states = nim.succ(state)
        print list_states
        state = nim.random_move(list_states)
nim.U_terminal(state)






