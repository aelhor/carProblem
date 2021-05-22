'''
    [
        ['x', 'x', 'x', 'x', 'x', 'x'],

        ['x', ' ', ' ', ' ', ' ', 'x'],

        ['x', ' ', ' ', 'S', ' ', 'x'],

        ['x', ' ', ' ', ' ', '#', 'x'],

        ['x', ' ', ' ', ' ', ' ', 'x'],

        ['x', 'x', 'x', 'x', 'x', 'x'] 
   ]
'''
import random
def getDirection(x, y, n) : 
    dirctions = []
    if x in range(1, n-2) : dirctions.append('v')
    if x in range(2, n-1) : dirctions.append('^')
    if y in range(1, n-2) : dirctions.append('>')
    if y in range(2, n-1) : dirctions.append('<')
    
    return dirctions
         

def createMaze(n) : 
    maze = [['.']*n for _ in range(n)]
    ## append the Xs
    for i in range(n) :  
        for j in range(n) : 
            maze[i][j] = random.choice(['x', ' ', ' '])
            if i == 0 or i == n-1 : 
                maze[i] = ['x']* n 
            if j == 0 or j == n-1  : 
                maze[i][j] = 'x'
    
    ## choose the goal 
    rand_i = random.randint(1, n-2)
    rand_j = random.randint(1, n-2)
    maze[rand_i][rand_j] = '#'
    print('goal',rand_i, rand_j)
    
    # choose start postion 
    startX = random.randint(1, n-2)
    startY = random.randint(1, n-2)
    print('start',startX, startY)

    dirctions = getDirection(startX, startY, n)  
    maze[startX][startY] = dirctions[0]
        
    return maze  
    
def printMaze(maze) :
    for i in maze:
        for j in i:
            print(j, end=' ')
        print() 
            
            
maze = createMaze(6)        
printMaze(maze)
print(maze)
