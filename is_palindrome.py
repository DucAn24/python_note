
def isPalindrome(s):
    s2 = "".join(char.lower() for char in s if char.isalnum())
    return s2 == s2[::-1]

s = input()
print(isPalindrome(s))