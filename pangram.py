def pangram(sentence):
    """Checks if a word or sentence has all alphabets."""
    # A set stores unique values.
    letters = set()

    for character in sentence:
        # Checks if the character is a alphabet.
        if character.isalpha():
            letters.add(character.lower())

    # Returns true if letters has all the alphabets.
    return len(letters) == 26


test_1 = pangram("abcdefg hijklmnopqrstuvwxyz")
print(test_1)

test_2 = pangram("time")
print(test_2)
