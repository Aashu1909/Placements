
import time
begin=time.time()

# Here we have to check x clockwise rotation in str1 and str2 
# we can reduce this problem in pattern searching algo 
# In a circular way we have to search a string in another one

# here idea is to concatinate s1+s1 and find s2
def check_rotation(str1,str2):
    if len(str1)!=len(str2):
        return False
    temp=str1+str1
    
    if str2 in temp:
        return False
    return False
    





str1=""
str2=""
print(check_rotation(str1,str2))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")