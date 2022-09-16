# As string are immutable we cannot change the given string 
# for that we have to create the new string

def reverse_a_string(s):
    reverse=""
    for char in s:
        reverse=char+reverse
    return reverse

s_input=input("Enter your string:")
print(reverse_a_string(s_input))
# now using string slicing technique
print(s_input[::-1])