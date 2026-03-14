from collections import Counter

def keyword_density(text):

    words = text.lower().split()

    freq = Counter(words)

    common = freq.most_common(10)

    return common