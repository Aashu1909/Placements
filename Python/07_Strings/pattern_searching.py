txt=input('Enter the pattern')
pat=input('Enter the pattern')
position=txt.find(pat)
while position>=0:
    print(position)
    position=txt.find(pat,position+1)