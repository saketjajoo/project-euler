import math
import requests
import utils

def get_upper_limit(num):
    return -1 + math.ceil(math.sqrt(1 + 4 * 1 * (num * 2)))

def is_triangle_word(word):
    word_number = 0
    for ch in word:
        word_number += ord(ch) - 65 + 1
    if word_number in utils.get_triangle_numbers(get_upper_limit(word_number)):
        return True
    return False

res = requests.get('https://projecteuler.net/resources/documents/0042_words.txt')
words = res.text.strip().replace('"', '').split(',')
count = 0
for i in range(len(words)):
    if is_triangle_word(words[i]):
        count += 1
print(count) # 162