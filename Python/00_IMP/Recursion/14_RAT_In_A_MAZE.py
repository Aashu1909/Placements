
def isValid(x,y,grid):
    if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1:
        return True
    return False
def ratInMaze(x,y,grid,solGrid):
    if x==len(grid)-1 and y==len(grid[0])-1:
        solGrid[x][y]=1
        return True
    if isValid(x,y,grid):
        solGrid[x][y]=1
        # Down
        if ratInMaze(x+1,y,grid,solGrid):
            return True
        # Right
        if ratInMaze(x,y+1,grid,solGrid):
            return True
        solGrid[x][y]=0
        return False
    return False

if __name__=="__main__":
    # n=int(input())
    maze=[
        [1,0,1,0,1],
        [1,1,1,1,1],
        [0,1,0,1,0],
        [0,0,0,1,1],
        [1,1,1,0,1]
    ]
    n=len(maze)    
    solMaze=[[0 for _ in range(n)] for _ in range(n)]
    start_x,start_y=0,0
    ratInMaze(start_x,start_y,maze,solMaze)
    for i in solMaze:
        print(i)