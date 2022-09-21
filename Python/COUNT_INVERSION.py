class Solution:
    def inversionCount(self, arr, n):
        # Your Code Here
        low=0
        high=n-1
        return self.mergeSort(arr,low,high)
    
    def mergeSort(self,arr,low,high):
        inv=0
        if low<high:
            mid=(low+high)//2
            inv+=self.mergeSort(arr,low,mid)
            inv+=self.mergeSort(arr,mid+1,high)
            inv+=self.merge(arr,low,mid,high)
        return inv
        
    def merge(self,arr,low,mid,high):
        inv=0
        left=arr[low:mid+1]
        right=arr[mid+1:high+1]
        k=low
        i=j=0
        while (i<len(left)) and (j<len(right)):
            if left[i]<right[j]:
                arr[k]=left[i]
                k+=1
                i+=1
            else:
                arr[k]=right[j]
                inv+=(len(left)-i)
                j=j+1
                k=k+1
                
        while (i<len(left)):
            arr[k]=left[i]
            k=k+1
            i=i+1
        while (j<len(right)):
            arr[k]=right[j]
            j+=1
            k+=1
        return inv
            
test_case=[10,5,30,15,7]
Merge_sort(test_case,left=0,right=len(test_case)-1)
print(test_case)
