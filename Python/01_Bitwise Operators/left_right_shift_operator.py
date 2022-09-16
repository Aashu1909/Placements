a=3
# Left shift Operator
# results in x*pow(2,y)
# Inshort leftshift operator x<<y 
print('Left Shift Operator')
print(f"A = {bin(a).replace('0b','')}")
print(f"A<<1 = {bin(a<<1).replace('0b','')} decimal value {a<<1}")
print(f"A<<2 = {bin(a<<2).replace('0b','')} decimal value {a<<2} ")
# Right Shift operator
a=33
print('Right Shift Operator')
print(f"A = {bin(a).replace('0b','')} = {a}")
print(f"A>>1 = {bin(a>>1).replace('0b','')} decimal value {a>>1}")
print(f"A>>2 = {bin(a>>2).replace('0b','')} decimal value {a>>2} ")
# Inshort RightShift operator x>>y 
# results in x//pow(2,y)
