from collections import deque
#Function to find whether a path exists from the source to destination.

def valid(x,y,n):
    if (x<0 or x>=n) or (y<0 or y>=n):
        return False
    return True

def is_Possible(grid):
    #Code here
    #First we are trying to find the source in the given grid
    n=len(grid)
    m=int(n)
    queue=deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                queue.append((i,j))
                break
    # Since we can move in only 4 direction left right up down
    dr=[(1,0),(0,1),(-1,0),(0,-1)]
    while len(queue)>0:
        cord=queue.popleft()
        x=cord[0]
        y=cord[1]
        for dx,dy in dr:
            nx=x+dx
            ny=y+dy
            if valid(nx,ny,n):
                if grid[nx][ny]==2:
                    return True
                if grid[nx][ny]==3:
                    grid[nx][ny]=1
                    queue.append((nx,ny))
    return False
                                    
    
    