import re, sys
from pathlib import Path
from pprint import pprint

folder = './richardson_clarissa_wordcount/'
Path(folder).mkdir(parents=True, exist_ok=True)

word_count_dict = {}
feed_document = sys.stdin

for line_in_document in feed_document:
    line_in_document = re.sub(r'^\W+|\W+$','', line_in_document)
    words_in_line = re.split(r'\W+', line_in_document)

    for word in words_in_line:
        word = word.lower()
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

pprint(word_count_dict)