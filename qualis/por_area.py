import csv
from slugify import slugify

f=csv.reader(file('latest.csv'), delimiter="\t")
areas = {}
#cabecalhos
header = "\t".join(f.next())


try:
	while True:
		line = f.next()
		#print f.line_num, line
		issn = line[0].rstrip()
		name = line[1].rstrip()
		qualis = line[2].rstrip()
		area = line[3].rstrip()
		atualizado = line[4].rstrip()

		key = slugify(line[3].rstrip())
		if key not in areas.keys():
			areas[key] = []
		areas[key].append("\t".join([issn, name, qualis, area, atualizado]))
except StopIteration:
	pass

for key, area in areas.items():
	h = file('areas/' + key + '.csv', 'w')
	h.write(header + '\n')
	for line in area:
		h.write(line + '\n')
	h.close()
