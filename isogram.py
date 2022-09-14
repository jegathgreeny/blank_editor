def isogram(word):
    """Checks if a word has only unique characters."""
    # A set can only store unique characters.
    letters = set()
    # To make the word case insensitive.
    word = word.lower()

    for character in word:
        # Skips non-alphabet words.
        if not character.isalpha():
            continue
        # Checks for repetition.
        if character in letters:
            return False

        letters.add(character)

    return True


test = isogram("orb123")
print(test)
