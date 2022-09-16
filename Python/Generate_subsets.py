# We are given a nums we have to return a a nums of nums
# such that we return nums (nums of subsets)
# Lets consider [1,2,3] size=3 numberofSubsets=2^3 or 1<<size
#    [1,2,3]  they are the subnet mask
# 0 = 0 0 0 []
# 1 = 0 0 1 [3]
# 2 = 0 1 0 [2]
# 3 = 0 1 1 [2,3]
# 4 = 1 0 0 [1]
# 5 = 1 0 1 [1,3]
# 6 = 1 1 0 [1.2]
# 7 = 1 1 1 [1,2,3]
# Time complexity o(numofSubset*size) space o(n*n)
def subsets_using_bit(nums):
    size=len(nums)
    numOfSubsets=1<<size
    all_subsets=[]
    for subnetMask in range(numOfSubsets):
        subset=[]
        for j in range(size):
            if (subnetMask &(1<<j))!=0:
                subset.append(nums[j])
        all_subsets.append(subset)
    return all_subsets

test_case=[10,5,15,46]
print(sorted(subsets_using_bit(test_case)))