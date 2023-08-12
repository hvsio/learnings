import os
from collections import defaultdict

def find_longest_word(filename) -> str:
    with open(filename) as f:
        words = {word: len(word) for word in f.read().split(' ')}
    return sorted(words.items(), key=lambda x: x[1], reverse=True)[0]

def find_all_longest_words(path) -> dict:
    return { filename.name:  find_longest_word(filename.path)[1] for filename in os.scandir(path)}



print(find_longest_word('/Users/alicjaharaszczuk/Desktop/sample/DWSample3-TXT.txt'))
print(find_all_longest_words('/Users/alicjaharaszczuk/Desktop/sample'))