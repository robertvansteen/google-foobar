def solution(input):
    decrypted = []

    for character in input:
        if character.isalpha() and character.islower():
            # Get the index of the character in the alphabet.
            character_index = ord(character) - ord('a')
            # Get the unicode position of the original character character.
            character_original_position = (25 - character_index) + ord('a')
            # Grab the original character based on the unicode position.
            character_original = chr(character_original_position)

            decrypted.append(character_original)
        else:
            decrypted.append(character)

    return ''.join(decrypted)
