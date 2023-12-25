import re
from collections import Counter

def mostCommonWord(paragraph: str, banned: [str]) -> str:
    words = re.findall(r'\w+', paragraph.lower())
    w_count = Counter(words)

    max = 0
    res = ''
    for word, count in w_count.items():
        if word not in banned and count > max:
            max = count
            res = word

    return res


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

aha = mostCommonWord(paragraph, banned)
print(aha)