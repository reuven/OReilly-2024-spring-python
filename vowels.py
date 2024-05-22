print(f'Hello from {__name__}!')

def count_vowels(s):
    total = 0
    for one_character in s:
        if one_character in 'aeiou':
            total += 1
    return total

print(f'Goodbye from {__name__}!')


