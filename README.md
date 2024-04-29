# Palindrome_Checker

This Python program contains a function named isPalindrome that checks if a given string is a palindrome.

isPalindrome(s): This function takes a string s as input and returns a boolean value indicating whether the string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

The function first removes all non-alphanumeric characters from the string and converts it to lowercase. It then checks if the resulting string is the same when reversed. If it is, the function returns True, indicating that the string is a palindrome. Otherwise, it returns False.

In the provided example, the function is used to check if the string “A man, a plan, a canal: Panama” is a palindrome. The function should print True because this string, when all non-alphanumeric characters are removed and it’s converted to lowercase, reads the same forward and backward.

This function can be useful in various applications such as natural language processing, data analysis, and more. Please note that the function considers an empty string as a palindrome.
