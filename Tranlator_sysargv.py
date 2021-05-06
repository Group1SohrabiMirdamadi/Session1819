import translators as ts
import sys
import argparse

if __name__ == '__main__':

    first_file, second_file, from_language, to_language, provider = sys.argv[1:]
    with open(first_file, 'r') as file:
        text = file.read()
        with open(second_file, 'w') as file2:
            result = str(getattr(ts, provider)(text, from_language=from_language, to_language=to_language))
            print(result)
            file2.write(result)

