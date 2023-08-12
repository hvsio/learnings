from collections import Counter
#counter sorts itself

def count_letters(s: str):
    return Counter(s).most_common(1)[0][1]

def most_repeating_word(strings: list):
    return max(strings, key=lambda x: count_letters(x))



print(most_repeating_word(['this', 'is', 'an', 'elementary', 'test', 'example']))