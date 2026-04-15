vowels = ("a","e","i","o","u")

word =(input("Please choose any word."))

vowel = 0

for i in (word):
    if i in vowels:
        print(i)
        vowel = vowel+1

if vowel == 0:
    print("there are no vowels in the given string")
else:
    print("the number of vowels in the givin string is:",vowel)