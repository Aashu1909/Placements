def maxSumIS(self, Arr, n):
    # code here
    def solve(index,prev_idx):
        if index==n:
            return 0
        sm=0
        if prev_idx==-1 or Arr[index]>Arr[prev_idx]:
            sm+=Arr[index]+solve(index+1,index)
        notSm=solve(index+1,prev_index)
        return max(sm,notSm)
    return solve(0,-1)
    