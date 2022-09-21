class Solution:
    def rev(self,st,arr,index):
        if len(st)==0:
            for i in range(index):
                st.append(arr[i])
            return
        arr[index]=st.pop()
        self.rev(st,arr,index+1)

    def reverse(self,st): 
        #code here
        arr=[0]*len(st)
        self.rev(st,arr,0)
        return st