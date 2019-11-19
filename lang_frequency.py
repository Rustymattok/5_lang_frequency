import argparse
import re
import collections
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        text_string = file_handler.read()
    return text_string


def get_most_frequent_words(text_string):
    num_words = 10
    text_lower = text_string.lower()
    match_pattern = re.findall(r'\b[\w]{2,15}\b', text_lower)
    words_top_ten = collections.Counter(match_pattern).most_common(num_words)
    return words_top_ten


def print_words(words_list):
    for word_and_count in words_list:
        print(*word_and_count, sep=' : ')


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--file',
        required=True,
        help='command - input file'
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    try:
        text_string = load_data(args.file)
        words = get_most_frequent_words(text_string)
        print_words(words)
    except ValueError:
        print('not correct format')


if __name__ == '__main__':
    main()
