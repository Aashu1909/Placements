def solution(binary_str,len_str,in_dis,in_state):
    total_time=0
    if len(binary_str)==len_str:
        for letter in binary_str:
            if letter=="0":
                # interdistrict
                total_time+=in_dis
            else:
                total_time+=in_state
        return total_time
    else:
        return total_time

if __name__=='__main__':
    no_test_case=int(input())
    while no_test_case>0:
        n,a,b=list(map(int,input().split(" ")))
        bin_str=input()
        ans=solution(binary_str=bin_str,len_str=n,in_dis=a,in_state=b)
        print(ans)
        no_test_case-=1
