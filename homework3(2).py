word = input("Enter a word: ")

result = ""

for character in word:
    if character.lower() in "aeiou":
        result += "*"
    else:
        result += character

print("The string with the vowels replaced is:", result)