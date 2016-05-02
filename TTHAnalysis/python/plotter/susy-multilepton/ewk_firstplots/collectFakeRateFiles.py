path = "mca_ewkino.txt"

f = open(path, "r")
ll = f.readlines()
f.close()

buffer = []
for l in ll:
	pos = l.find("FakeRate=\"")
	if pos == -1: continue
	string = l[pos+10:]
	string = string[:string.find("\"")]
	ss = string.split("\,")
	ss = [s[s.rfind("/")+1:] for s in ss]
	for s in ss:
		if not s in buffer:
			buffer.append(s)

for b in buffer:
	print b 
