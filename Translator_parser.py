import translators as ts
import sys
import argparse
import os

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Translator Description')

    parser.add_argument('file_path', action='store', metavar='FILE_PATH', help='Directory Path for Reading File',
                        nargs='?')
    parser.add_argument('-s', '--save', action='store', metavar='SAVE_PATH', default='',
                        help='Directory Path for Writing in File')
    parser.add_argument('-f', '--from_lang', action='store', metavar='FROM_LANG', default='auto',
                        help='Language Origin')
    parser.add_argument('-t', '--to_lang', action='store', metavar='TO_LANG', default='fr', help='Language Destination')
    parser.add_argument('-p', '--provider', action='store', metavar='PROVIDER', choices=['google', 'bing'],
                        default='google', help='Choose Provider')

    args = parser.parse_args()

    text = ""
    if args.file_path is None:
        while True:
            try:
                text += f"{input('>>')}\n"
            except KeyboardInterrupt:
                with open(args.save, 'w') as file2:
                    result = str(getattr(ts, args.provider)(text, from_language=args.from_lang, to_language=args.to_lang))
                    print(result)
                    file2.write(result)
                break

    else:
        with open(args.file_path, 'r') as file:
            text = file.read()
            with open(args.save, 'w') as file2:
                result = str(getattr(ts, args.provider)(text, from_language=args.from_lang, to_language=args.to_lang))
                print(result)
                file2.write(result)
