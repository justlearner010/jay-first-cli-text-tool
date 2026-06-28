from collections import Counter

# collection counter版本

def word_freq_cnt(text, top_n):
    if top_n < 0:
        raise ValueError("Top value is invalid")

    words = [word.lower() for word in text.split()]
    counter = Counter(words)

    top_words = counter.most_common(top_n)

    return top_words

def count_words(text, word):
    target_word = word.strip().lower()

    words = [item.lower() for item in text.split()]

    counter = Counter(words)
    return counter.get(target_word, 0)
