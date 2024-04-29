def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
