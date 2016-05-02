list = ""
srs  = ""
for i in range(1,60+1):
	list += "\"1,"+str(i-1) + ".5,"+str(i)+".5\" " 
	srs  += "\"SR"+str(i)+"\" "

print list
print srs
