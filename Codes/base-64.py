import argparse
from base64 import b64encode, b64decode

parser = argparse.ArgumentParser(description='Encode or decode a word in base64')
group = parser.add_mutually_exclusive_group()
group.add_argument('-e', '--encode', action='store_true', help='encode the word in base64')
group.add_argument('-d', '--decode', action='store_true', help='decode the word from base64')
parser.add_argument('word', type=str, help='the word to encode or decode in base64')

args = parser.parse_args()

if args.encode:
    encoded_word = b64encode(args.word.encode('utf-8')).decode('utf-8')
    print(f"Encoded word: {encoded_word}")
elif args.decode:
    decoded_word = b64decode(args.word.encode('utf-8')).decode('utf-8')
    print(f"Decoded word: {decoded_word}")
else:
    print("Please specify either -e or -d to encode or decode the word in base64.")