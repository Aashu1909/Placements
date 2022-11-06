import collections
#This problem cannot be solved using dfs because it will travel to all the depth in the matrix
#  And we want to traverse level by level
def orangesRotting(grid) -> int:
    cnt_fresh=0
    n,m=len(grid),len(grid[0])
    x,y=0,0
    queue=collections.deque()
    visited=[[0 for _ in range(m)] for _ in range(n)]
    #firstly append the cordinates of rotten oranges in the queue from the grid
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                queue.append([i,j,0])
                visited[i][j]=2
            if grid[i][j]==1:
                cnt_fresh+=1
    
    #There can only 4 direction since it can move vertical horizontal only
    directions=[(-1,0),(1,0),(0,1),(0,-1)]
    tm=0
    cnt=0
    #BASIC BFS TRAVERSAL
    while len(queue)>0:
        x,y,time=queue.popleft()
        tm=max(tm,time)
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if nx>=0 and nx<n and ny>=0 and ny<m and visited[nx][ny]!=2 and grid[nx][ny]==1:
                queue.append([nx,ny,time+1])
                visited[nx][ny]=2
                cnt+=1        
    
    if cnt!=cnt_fresh:
        return -1
    return tm