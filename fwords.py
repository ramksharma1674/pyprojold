def fetch_words(url):
	"""Fetch a list of words from a URL. """
	with urlopen(url) as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf8').split()
			for word in line_words:
				story_words.append(word)
	return story_words
	
new_words = []
new_words = fetch_words("https://app.pluralsight.com/player?course=python-fundamentals&author=austin-bingham&name=python-fundamentals-m00-welcome&clip=1")
print (new_words)