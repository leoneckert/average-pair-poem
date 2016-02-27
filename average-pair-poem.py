import sys
import random
import re


text1 = open(sys.argv[1])
words1 = list();

for line in text1:
	line = line.strip();
	words = line.split();

	# words_clean = list();
	# for w in words:
	# 	# print w
	# 	w = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', '', w)
	# 	print w
	# 	words_clean.append(w)

	# print words
	if words != []:
		words1 = words1 + words

# w = words1.sort(key=len, reverse=True)
w = sorted(words1, key=len)
# print w

averagelength = 0
for i in range(len(w)/2):
	p = w[i] + " " + w[-i]
	averagelength += len(p)

averagelength /= len(w)/2

the_selected_strings = list()

for i in range(len(w)/2):
	p = w[i] + " " + w[-i]
	if (len(p) == averagelength):
		# print p
		the_selected_strings.append(p)

# print the_selected_strings
print "\n"


for i in range(10):

	print random.choice(the_selected_strings) + " - " + random.choice(the_selected_strings)
	# if random.uniform(0.0, 1.0) < 0.8:
	# 	print random.choice(the_selected_strings),
	# else:
	# 	print " " * averagelength,
	# print "-",
	# if random.uniform(0.0, 1.0) < 0.8:
	# 	print random.choice(the_selected_strings)
	# else:
	# 	print " " * averagelength


print "\n"