# Rabin Karp algorothm is also Quadratic in worst case but it Works Better in general
# Like naive algorihm we slide the window ONE By ONE
# Here we Compare hash value of the pattern with the current text window,
# after then only comapre individual character this way we safe effectively when we a big pattern
# input txt and pat
# Rabin-Karp algorithm in python
d = 10
def search(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0
    # precomputing D^m-1
    for i in range(m-1):
        h = (h*d) % q
    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    # Find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1 #One Based Indexing
            if j == m:
                print("Pattern is found at position: " + str(i+1))
        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
            if t < 0:
                t = t+q
text = "ABCCDDAEFG"
pattern = "CDD"
q = 13
search(pattern, text, q)
    