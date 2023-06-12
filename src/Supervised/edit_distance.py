import re

def normalize_whitespace(text):
    return re.sub(r'\s+', ' ', text)
def remove_nonalphanumeric_or_space(text):
    return re.sub(r'[^a-zA-Z0-9 ]', '', text)
def preprocess(text):
    return remove_nonalphanumeric_or_space(normalize_whitespace(text.strip())).lower().split(' ')


def within_one(first, second):
    first = preprocess(first)
    second = preprocess(second)

    print(first, second)

    f = len(first); s = len(second)

    if abs(f - s) > 1: #would need to add/remove more than one character
        return False
    
    n = min(f, s)
    x = max(f, s)

    i = 0; j = 1
    while i < n and first[i] == second[i]:
        i += 1
    while j < n and first[-j] == second[-j]:
        j += 1
    j -= 1

    print(i, j)

    return i + j >= x - 1
