#Write a program that receives on the first line words separated by a space and a searched
# palindrome on the second. Print all the palindromes on the first line. Print all the
# occurrences of the searched palindrome in the format: "Found palindrome {count} times"
command = input()
palindrome = input()
palindromes= []
command = command.split()
for i in command:
    if i == i[::-1]:
        palindromes.append(i)
occurrences = palindromes.count(palindrome)
print(palindromes)
print(f"Found palindrome {occurrences} times")
