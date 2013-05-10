from sys import argv

script, filename = argv

opened = open(filename)

read_text = opened.readlines()

scores_text = [alter.strip() for alter in read_text]

d = {}

for i in scores_text:
	splitter = i.split(':')
	d[splitter[0]] = (splitter[1])
	
for f in sorted(d.iteritems()):
	print f
	


