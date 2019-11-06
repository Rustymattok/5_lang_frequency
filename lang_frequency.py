import re


def load_data(filepath):
    if filepath[-4:len(filepath)] != '.txt':  # condition for format txt.
        print('not correct format')
        return
    with open(filepath) as f:
        text = f.read()
    return text


def get_most_frequent_words(text):
    text = text.lower()
    match_pattern = re.findall(r'\b[\w]{2,15}\b', text)
    words = {}
    for word in match_pattern:
        count = words.get(word, 0)
        words[word] = count + 1
    words_list = list(words.items())
    # sort words by count max -> min.
    words_list.sort(key=lambda i: i[1], reverse=True)
    return words_list  # list words (word:count}) sorted.


if __name__ == '__main__':
    file = input('enter file way: ')
    try:
        text_file = load_data(file)
        sorted_list = get_most_frequent_words(text_file)
        for word in sorted_list[:10]:  # to show only 10 words.
            print(word[0], word[1])
    except FileNotFoundError:
        print("not found file")
