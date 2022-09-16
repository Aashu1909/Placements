def max_heapify(arr,size,index):
    largest=index
    left_child=2*index+1
    right_child=2*index+2
    if (left_child < size) and ( arr[largest] < arr[left_child] ):
        largest=left_child
    if ( right_child < size ) and (arr[largest]<arr[right_child]):
        largest=right_child
    if  (largest!=index):
        arr[largest],arr[index]=arr[index],arr[largest]
        max_heapify(arr,size,largest)
    
def build_heap(arr,size):
    leftmost_parent=((size-1)-1)//2
    for i in range(leftmost_parent,-1,-1):
        max_heapify(arr,size,i)

def heap_sort(arr,n):
    build_heap(arr,n)
    for i in range(n-1,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
        max_heapify(arr,i,0)

arr=[90,55,12,14,2,3,65,5,1,0]
heap_sort(arr,len(arr))
print(arr)