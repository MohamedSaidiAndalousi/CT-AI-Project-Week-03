def swap(word1: str, word2: str) -> str:
    new_word1 = word2[:2] + word1[2:]
    new_word2 = word1[:2] + word2[2:]

    return new_word1 + " " + new_word2


print(swap("Feliks", "goy"))