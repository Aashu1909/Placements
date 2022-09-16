# Tower of hanoi is a problem where we have to find the number of Moves
# Required to Move N number of disk from tower A to C
# using B as an Auxilliary

#     |      |       |  
#    _|_    _|_     _|_   
#    A       B      C
 
def tower_of_hanoi(N,A,B,C):
    if N==1:
        print('Move '+str(N)+' from '+ A +' to '+ C)
        return
    tower_of_hanoi(N-1,A,C,B)
    print('Move '+str(N)+' from '+A+' to '+ C)
    tower_of_hanoi(N-1,B,A,C)

start="A"
aux="B"
end="C"
tower_of_hanoi(4,start,aux,end)