from collections import Counter

# collection counter版本

def word_freq_cnt(fname, top_n=10):
    with open(fname, 'r') as f:

        words = [word.lower() for line in f for word in line.strip().split()]


    counter = Counter(words)

    top_words = counter.most_common(top_n)

    return top_words
