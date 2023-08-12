import pyuca  # pyuca does not take the locale into account
import unicodedata
from unicodedata import normalize
import locale
from unicodedata import name
import sys
import array
import codecs

codecs.register_error('custom_error', lambda x: (f"Custom error", x.start + 1))
print(bytes.fromhex('31 4B CE A9'))
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)

'''
'xmlcharrefreplace' replaces unencodable characters with an XML entity.
If you can’t use UTF, and you can’t afford to lose data, this is the only option.
'''
city = 'São Paulo'
print(city.encode('cp437', errors='custom_error'))


print(open('cafe.txt', 'w', encoding='utf_8').write('café'))
print(open('cafe.txt').read())


print(sys.version)
print()
print('sys.stdout.isatty():', sys.stdout.isatty())
print('sys.stdout.encoding:', sys.stdout.encoding)
print()

test_chars = [
    '\N{HORIZONTAL ELLIPSIS}',       # exists in cp1252, not in cp437
    '\N{INFINITY}',                  # exists in cp437, not in cp1252
    '\N{CIRCLED NUMBER FORTY TWO}',  # not in cp437 or in cp1252
]

for char in test_chars:
    print(f'Trying to output {name(char)}:')
    print(char)


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())


s1 = 'café'
print(normalize('NFD', s1), normalize('NFD', s1).encode('ascii', 'ignore').decode('ascii'))
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
print(
    len(s1), len(s2),
    len(normalize('NFC', s1)), len(normalize('NFC', s2)),
    len(normalize('NFD', s1)), len(normalize('NFD', s2)),
    normalize('NFC', s1) == normalize('NFC', s2),
    normalize('NFD', s1) == normalize('NFD', s2),
    normalize('NFD', s1), normalize('NFD', s2),
)

my_locale = locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
print(my_locale)
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)

coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)


START, END = ord(' '), sys.maxunicode + 1


def find(*query_words, start=START, end=END):
    query = {w.upper() for w in query_words}
    for code in range(start, end):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name and query.issubset(name.split()):
            print(f'U+{code:04X}\t{char}\t{name}')


def main(words):
    if words:
        find(*words)
    else:
        print('Please provide words to find.')


if __name__ == '__main__':
    main(sys.argv[1:])
