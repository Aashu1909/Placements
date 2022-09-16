

a=13
b=4
# Bitwise AND Operator
print(f"A {bin(a).replace('0b','')} & B {bin(b).replace('0b','')}={a&b}")
# Bitwise OR
print(f"A({bin(a).replace('0b','')}) | B ({bin(b).replace('0b','')})={a|b}")
# BITwise NOT
print(f"A {bin(a).replace('0b','')} = {~a}")
# Bitwise XOR
print(f"A ^ B {bin(a).replace('0b','')} ^ {bin(b).replace('0b','')} = {a^b}")