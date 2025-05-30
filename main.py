from stats import get_num_words, char_count, report_01
import sys

args = sys.argv
if len(args) == 2:
	script = args[0]
	book_path = args[1]
else:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)


def get_book_text(book_path):
	with open(book_path) as f:
		file_contents = f.read()
		print(file_contents)


def main(book_path):
	# book_path = 'books/frankenstein.txt'
	report_01(book_path)

main(book_path)
