def is_palindrome(string,start,end):
    if start>=end:
        return True
    return string[start]==string[end] and is_palindrome(string,start+1,end-1)

string="abba"
print(is_palindrome())