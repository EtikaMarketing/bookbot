def get_num_words(book_path):
	with open(book_path) as f:
		file_contents = f.read()
		words = []
		words = file_contents.split(None,-1)
		num_words = len(words)
		return num_words

def char_count(book_path):
	with open(book_path) as f:
		file_contents = f.read()
		file_contents = file_contents.lower()
		characters = []
		characters = list(file_contents)
		uniques = set(file_contents)
		uniques_count = set()
		for unique in uniques:
			count = 0
			for i in characters:
				if unique == i:
					count += 1
			counted = (f"'{unique}': {count},")
			uniques_count.add(counted)
		print(uniques_count)
		
def myFunc(e):
  return e['num']


def report_01(book_path):
	with open(book_path) as f:
		file_contents = f.read()
		file_contents = file_contents.lower()
		characters = []
		characters = list(file_contents)
		uniques = set(file_contents)
		uniques_count = set()
		pair = dict()
		for unique in uniques:
			count = 0
			for i in characters:
				if unique == i and unique.isalpha() == True:
					count += 1
					pair[unique] = count
		pair_sorted = sorted(pair.items(), reverse=True, key=lambda kv: (kv[1], kv[0]))
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {book_path}...")
		print("----------- Word Count ----------")
		print(f"Found {get_num_words(book_path)} total words")
		print("--------- Character Count -------")
		for i in pair_sorted:
			print(f"{i[0]}: {i[1]}")
		print("============= END ===============")
