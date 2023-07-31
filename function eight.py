def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

print(is_palindrome("radar")) 
print(is_palindrome("Python")) 
