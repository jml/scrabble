"""Tools to help you cheat at Scrabble."""

import os


SOWPODS_FILE = os.path.join(
    os.path.dirname(__file__), 'source_data/sowpods.txt')

WORDS_FILE = '/usr/share/dict/words'


def generate_words(dictionary):
    fd = open(dictionary, 'r')
    for line in fd:
        yield line.strip().lower()
    fd.close()


def load_dictionary(dictionary):
    return set(generate_words(dictionary))


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    return is_subanagram(word1, word2)


def is_subanagram(small, large):
    duplicates = list(large)
    for character in small:
        if character not in duplicates:
            return False
        duplicates.remove(character)
    return True


def factorial(n):
    ret = 1
    while n > 0:
        ret *= n
        n -= 1
    return ret


def generate_permutations(sequence):
    sequence = list(sequence)
    if len(sequence) == 1:
        yield sequence
    else:
        for index, element in enumerate(sequence):
            sub_perms = generate_permutations(
                sequence[:index] + sequence[index+1:])
            for permutation in sub_perms:
                yield [element] + permutation


def get_possible_anagrams(word):
    return set([''.join(permutation)
                for permutation in generate_permutations(word)])


def find_anagrams_by_permutations(dictionary, word):
    for permutation in get_possible_anagrams(word):
        permutation = ''.join(permutation)
        if permutation in dictionary:
            yield permutation


def find_anagrams_by_dictionary(dictionary, word):
    for candidate in dictionary:
        if is_anagram(word, candidate):
            yield candidate


if __name__ == '__main__':
    import sys
    dictionary = load_dictionary(SOWPODS_FILE)
    for anagram in find_anagrams_by_permutations(dictionary, sys.argv[1].lower()):
        print anagram
