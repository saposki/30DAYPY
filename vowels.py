'''
    Write a program that counts up the number of vowels contained in the string s.
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
    your program should print: "Number of vowels: 5"
'''

list_of_vowels = ['a', 'e', 'i', 'o', 'u']
s = 'azcbobobegghakl'
count  = 0

for i in range(0, len(s)):
    if(s[i] in list_of_vowels):
        count += 1

print 'Number of vowels: %r' %(count)
