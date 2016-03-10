import sys


def caesar(n, text):
    output = ""
    n = n % 26
    for i in range(len(text)):
        if text[i].isalpha():
            char_code_A = ord('a')
            if text[i].isupper():
                char_code_A = ord('A')
            output += chr((ord(text[i]) - char_code_A + n) % 26 + char_code_A)
        else:
            output += text[i]
    return output


def main():
    n, text = sys.stdin.readlines()
    print caesar(int(n), text)

if __name__ == '__main__':
    main()
