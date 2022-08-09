import time

def dataToList(input: str):
	out = []
	for num in range(len(input)):
		out.append(input[num])
	return out

def listToScore(list: list, line, row) -> int:
	score = 0
	for count, i in enumerate(list):
		if i.isnumeric():
			score += int(i)
		elif len(list) == 5 and count == 0 and i == "n":
			score += 0
			# ignore score N/A for if not working
		else:
			print(f"Not added to list: {i} - LINE {line}; ROW {row}; POS: {count}")
	return score

def dataToScore(input: str, line: int, row: int) -> int:
	input = str(input)
	return listToScore(dataToList(input), line, row)


def getTime():
	return str(time.time()).split(".")[0]

def timeToLocal(epoch):
	print(time.ctime(int(epoch)))