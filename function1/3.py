def solve(numheads, numlegs):
    for numchickens in range(numheads + 1):
        numrabbits = numheads - numchickens
        totallegs = (numchickens * 2) + (numrabbits * 4)
        
        if totallegs == numlegs:
            return f"{numchickens} chickens and {numrabbits} rabbits."
    
    return "No solution found."
#Example:
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(result)