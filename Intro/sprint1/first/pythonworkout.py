import re
def ubbi_dubbi(word):
    return ''.join([ f'ub{letter}' if letter in ['a', 'e', 'i', 'o', 'u'] else letter for letter in word])

def ubbi_dubbi_replace(word):
    x = re.sub(r'([aeiou])', r'ub\1', word)
    return x



if __name__ == '__main__':
    print(ubbi_dubbi('octopus'))
    print(ubbi_dubbi('elephant'))

    print(ubbi_dubbi_replace('octopus'))
    print(ubbi_dubbi_replace('elephant'))