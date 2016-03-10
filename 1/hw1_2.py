import sys
import re
import random


def britishShuffle(text):
    output = []
    last_index = 0
    for wordCenter in re.finditer("(?<=\W\w)[\w]{2,}(?=\w\W)", text):
        output.append(text[last_index:wordCenter.start()])
        listToShuffle = list(wordCenter.group(0))
        random.shuffle(listToShuffle)
        output.append(''.join(listToShuffle))
        last_index = wordCenter.end()
    output.append(text[last_index:])
    return ''.join(output)


def main():
    input = sys.stdin.read()
    print britishShuffle(input)

if __name__ == '__main__':
    main()
