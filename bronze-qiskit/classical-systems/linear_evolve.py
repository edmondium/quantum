def linear_evolve(operator, state):
    newstate = []
    for i in range(len(operator)):
        newstate.append(0)
        for j in range(len(state)):
            newstate[i] += operator[i][j] * state[j]
    return newstate
