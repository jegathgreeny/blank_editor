def isogram(word):
    """Checks if a word is isogram. An isogram is a word with only unique characters."""
    # A set stores only unique characters.
    letters = set()
    # To make it case insensitive.
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
