import time
begin=time.time()

# Rabin Karp algorothm is also Quadratic in worst case but it Works Better in general
# Like naive algorihm we slide the window ONE By ONE
# Here we Compare hash value of the pattern with the current text window,
# after then only comapre individual character this way we safe effectively when we a big pattern

# input txt and pat

def rabinKarpAlgo(txt,pat):
    





txt=""
pat=""
print(rabinKarpAlgo(txt,pat))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")