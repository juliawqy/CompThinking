def is_palindrome(s):
    
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    if s[0] == s[len(s)-1]:
        return is_palindrome(s[1:len(s)-1])
    return False

print(is_palindrome("madam"),
is_palindrome("madame"),
is_palindrome("raccar"),
is_palindrome("raccars"),
is_palindrome("gomog"))