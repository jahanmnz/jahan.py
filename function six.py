def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if char in vowels:
        return True
    else:
        return False

characters = ['a', 'b', 'E', 'Z']
for char in characters:
    if is_vowel(char):
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")
