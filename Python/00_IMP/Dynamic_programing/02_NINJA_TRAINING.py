# there are 3 number of thing that a ninja does which gives a points
# each day a ninja does something ,Ninja cannot perform the same task for Two consecutive days
# find the maximum points that a ninja can achieve
# array=[[1,2,3],[10,2,12],[5,21,3],[5,15,23]]

# Recursion and memoization
def maxPoint(day,lastTask,points,dp):
    if day==0:
        maxx=0
        for task in range(3):
            if task!=lastTask:
                maxx=max(maxx,points[day][task])
        return maxx
    #Any other day
    if (day,lastTask) in dp:
        return dp[(day,lastTask)]
        
    maxx=0
    for task in range(3):
        if task!=lastTask:
            point=points[day][task]+maxPoint(day-1,task,points,dp)
            maxx=max(maxx,point)
    dp[(day,lastTask)]=maxx
    return maxx

# 0->n
def maxPoint2(day,lastTask,points,dp):
    if day==len(points)-1:
        maxx=0
        for task in range(3):
            if task!=lastTask:
                maxx=max(maxx,points[day][task])
        return maxx
    #Any other day
    if (day,lastTask) in dp:
        return dp[(day,lastTask)]
    maxx=0
    for task in range(3):
        if task!=lastTask:
            point=points[day][task]+maxPoint2(day+1,task,points,dp)
            maxx=max(maxx,point)
            
    dp[(day,lastTask)]=maxx
    return maxx 

# Tabulazation-Bottom up dp Tn O(N*4*3) S O(n*4)
def maxPoint1(points):
    row,col=len(points),len(points[0])
    dp=[[-1 for _ in range(col+1)] for _ in range(row)]
    #Day Task
    dp[0][0]=max(points[0][1],points[0][2])
    dp[0][1]=max(points[0][0],points[0][2])
    dp[0][2]=max(points[0][0],points[0][1])
    dp[0][3]=max(points[0][1],points[0][2],points[0][0])

    for day in range(1,row):
        for lastTask in range(col+1):
            dp[day][lastTask]=0
            maxi=0
            for task in range(col):
                if task!=lastTask:
                    point=points[day][task]+dp[day-1][task]
                    maxi=max(point,maxi)
            dp[day][lastTask]=maxi
    print(points)
    print(dp)
    return dp[row-1][col]

def main():
    nums=[[1,2,3],[10,2,12],[5,21,3],[5,15,23]]
    n=len(nums)
    dp={}
    # print(maxPoint(n-1,3,nums,dp))
    dp2={}
    print(maxPoint2(0,-1,nums,dp2))
    # print(maxPoint1(nums))

main()