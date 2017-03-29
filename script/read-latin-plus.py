with open("latin-plus.txt", "r") as f:
	lines = f.read().splitlines()
	for l in lines:
		split = l.split("\t")
		split.pop(0) # index
		#print split[0] # name
		if split[1]: # uni
			print split[1]