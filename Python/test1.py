from ast import Num
import time
begin=time.time()

# Ques
# test_case
# O/p

def MinRemovedElements(a, b, n):
	print(a,b,n)
	no_of_ones = 0;
	no_of_zeroes = 0;
	for i in range(n):
		if (a[i] == 1):
			no_of_ones += 1;
		else:
			no_of_zeroes += 1;
		if (b[i] == 1):
			no_of_ones += 1;
		else:
			no_of_zeroes += 1;
	diff1 = no_of_ones - no_of_zeroes;
	mp = {};
	mp[0] = 0;
	curr = 0;
	for i in range(n):
		print(curr)
		if (a[i] == 1):
			curr += 1;
		else :
			curr -= 1;

		if curr not in mp:
			mp[curr] = i + 1;
	curr = 0;
	answer = 2 * n;
	print(mp)
	for i in range(n):
		if (b[i] == 1):
			curr += 1;
		else:
			curr -= 1;
		print("curr",curr)
		if (diff1 - curr) in mp :
			answer = min(answer, i + 1 + mp[diff1 -
											curr]);

	if diff1 in mp:
		answer = min(answer, mp[diff1]);

	return answer;


# This code is contributed by Yash_R
s1="010110"
s2="111001"
a = [ 0, 1];
b = [ 1, 1];
# list(map(int,list(s1)))
# list(map(int,list(s1))),list(map(int,list(s2)))
print(MinRemovedElements(a,b,len(a)))


time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")