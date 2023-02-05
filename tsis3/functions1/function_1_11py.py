def is_palindrome(string):
    new_string=string[::-1]
    if new_string==string:
        print(True)
    else:
        print(False)
string=input()
is_palindrome(string)
