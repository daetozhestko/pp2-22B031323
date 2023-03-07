def IsPalindrome(s):
    rev=''.join(reversed(s))
    if s==rev:
        return True
    else:
        return False
s="abba"
print(IsPalindrome(s))