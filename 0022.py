import requests

def get_name_score(name):
    score = 0
    for char in name:
        score += ord(char) - 65 + 1
    return score

r = requests.get('https://projecteuler.net/resources/documents/0022_names.txt')
names = r.text.replace('"', '').split(',')
names.sort()
total_score = 0
for i in range(len(names)):
    total_score += (i + 1) * get_name_score(names[i])
print(total_score) # 871198282