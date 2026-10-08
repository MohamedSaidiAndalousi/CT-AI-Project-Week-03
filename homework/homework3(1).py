
word = input("Enter a word: ")

vowels = 0
consonants = 0

for character in word:
    if character.lower() in "aeiou":
        vowels += 1
    elif character.isalpha():
        consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)