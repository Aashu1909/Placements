# Tower of hanoi is a problem where we have to find the number of Moves
# Required to Move N number of disk from tower A to C
# using B as an Auxilliary

#     |      |       |  
#    _|_    _|_     _|_   
#    A       B      C
 
def tower_of_hanoi(N,A,B,C):
    if N==1:
        # cnt+=1
        print('Move '+str(N)+' from '+ A +' to '+ C)
        return
    tower_of_hanoi(N-1,A,C,B)
    print('Move '+str(N)+' from '+A+' to '+ C)
    # cnt+=1
    tower_of_hanoi(N-1,B,A,C)

def toh(self, N, fromm, to, aux):
        # Your code here
        if N==1:
            print('move disk {} from rod {} to rod {}'.format(N,fromm,to))
            return 1
        n1=N-1
        a=self.toh(n1,fromm,aux,to)
        print('move disk {} from rod {} to rod {}'.format(N,fromm,to))
        b=self.toh(n1,aux,to,fromm)
        return a+b+1

start="A"
aux="B"
end="C"
cnt=0
tower_of_hanoi(4,start,aux,end)
# print(cnt)
