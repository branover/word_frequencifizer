# -*- coding: utf-8 -*-
import optparse
import os
from pymystem3 import Mystem

opt_parser = optparse.OptionParser()

opt_parser.add_option("-i", "--input", dest="filename", default="sample\hp1-full", help="Read in from file")
opt_parser.add_option("-o", "--output", dest="outfile", help="Output to results to file")
opt_parser.add_option("-d", "--directory", dest="directory", help="Read in from every file in directory")
opt_parser.add_option("-q", "--quantity", default='True', dest="quantity", help="Add the quantity to the word or not. (set to True or False)")
opt_parser.add_option("-m", "--minimum", default=3, dest="minimum", help="Minimum number of occurences before showing a word")
opt_parser.add_option("-l", "--length", default=-1, dest="length", help="Maximum number of results to show (sorted by frequency)")
opt_parser.add_option("-e", "--exclude", dest="exclude", help="Load file with list of words to exclude from results (will also be converted to root word before comparison)")
(options, args) = opt_parser.parse_args()

text = ""
if options.directory:
    for name in os.listdir(options.directory):
        text += open(os.path.join(options.directory,name)).read().decode('utf-8')
else:
    f = open(options.filename)
    text = f.read().decode('utf-8')
    f.close()
exclude = ''
if options.exclude:
    f = open(options.exclude)
    exclude = f.read().split()
    f.close()


punct = u"…—–!\"#«»$%&\'()*+,./:;=>?@[\\]^_`{|}~"
text = u"".join(ch for ch in text if ch not in punct).lower()
m = Mystem()

word_dict = {}
n = 100000
text = text.split()
text = [text[i:i + n] for i in xrange(0, len(text), n)]

exclude = "".join(m.lemmatize(" ".join(exclude))).split()

print "Splitting text into: " + str(len(text)) + " chunks."
for chunk in text:
    chunk = " ".join(chunk)
    done = ''.join(m.lemmatize(chunk.encode('utf-8')))

    for word in done.split():
        if word not in word_dict:
            word_dict[word] = {}
            word_dict[word] = 1
        else:
            word_dict[word] += 1

sorted_word_dict = sorted(word_dict, key=word_dict.get, reverse=True)

output = ""
min = int(options.minimum)
for i, key in enumerate(sorted_word_dict):

    if word_dict[key] >= min:
        if i == options.length:
            break
        if options.exclude and (key in exclude):
            print "tet"
            continue
        if options.quantity and (options.quantity.lower() != 'false'):
            line = "%s,%s" % (key, word_dict[key])
        else:
            line = "%s" % key
        output += line+'\n'
print output
if options.outfile:
    f = open(options.outfile,'w')
    f.write(output)
    f.close()
