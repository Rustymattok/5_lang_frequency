import argparse
import re
import collections
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        data_text = file_handler.read()
    return data_text


def get_most_frequent_words(data_text):
    text = data_text.lower()
    match_pattern = re.findall(r'\b[\w]{2,15}\b', text)
    words_dict = collections.Counter()
    for word_single in match_pattern:
        words_dict[word_single] += 1
    return words_dict


def get_sorted_list_words(words_dict):
    words_list = []
    for word_single in dict(words_dict).items():
        words_list.append(word_single)
    words_list.sort(key=lambda i: i[1], reverse=True)
    return words_list


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        required=True,
                        help="command - input file")
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    try:
        file_data = load_data(args.file)
        words_dict = get_most_frequent_words(file_data)
        words_sorted = get_sorted_list_words(words_dict)
        for word in words_sorted:
            print(word[0], ": ", word[1])
    except ValueError:
        print("not correct format")


if __name__ == '__main__':
    main()
