import logging
logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s]: %(message)s')

def questionnaireScoring(inputs: list):
	PHQ = "---------"
	GAD = "-------"
	phobia = "---"
	WSAS = "-----"
	for count, i in enumerate(inputs):
		if i[1] == "P":
			if i[2] == "H":
				phobia = stringChar(phobia, i[4], i[3])
			else:
				PHQ = stringChar(PHQ, i[3], i[2])
		elif i[1] == "G":
			GAD = stringChar(GAD, i[3], i[2])
		elif i[1] == "W":
			WSAS = stringChar(WSAS, i[3], i[2])
		else:
			logging.error(f"Questionnaire input scoring: {i} @ {count}\n\t{inputs}")
	output = [PHQ, GAD, phobia, WSAS]
	return output

def getQuestionnaireOutput(values:list) -> list:
	output = []
	PHQ = "---------"
	GAD = "-------"
	phobia = "---"
	WSAS = "-----"
	scales = "------" # last of notes is 0-9, questionnaire is 1-10
	checks = "-----"
	extra = ""

	# use switch case?
	for _, val in enumerate(values):
		if val[1] in ["P", "G", "W"]:
			if values.get(val): # seperate from previous if statement to help debugging
				if val[1] == "P":
					if val[2] == "H":
						phobia = stringChar(phobia, val[4], val[3], True)
					else:
						PHQ = stringChar(PHQ, val[3], val[2], True)
						pass
				elif val[1] == "G":
					GAD = stringChar(GAD, val[3], val[2], True)
				elif val[1] == "W":
					WSAS = stringChar(WSAS, val[3], val[2], True)
		# ===========================================
		elif val[1] == "N": # sliders
			if val[2] == "5": # 0-9 rather than 1-10
				scales = stringChar(scales, str(int(getScaleOutput(val, values))-1), val[2])
			else: # 0-7
				scales = stringChar(scales, getScaleOutput(val, values), val[2])
		elif val[1:3] == "CB": # checkboxes
			checks = stringChar(checks, checkElem(val, values), val[3])
		elif val == "-EXTRAS-": # textbox
			extra = values.get(val)
		
	output = [PHQ, GAD, phobia, WSAS, scales, checks, extra]
	return output

def stringChar(str, char, pos, shift=False):
	"""
	pos start @ 0
	"""
	pos = int(pos)
	if shift:
		pos -= 1
	return str[:pos] + char + str[pos + 1:]

def checkElem(val, values):
	if values.get(val):
		return "1"
	elif not values.get(val):
		return "0"
	else:
		logging.info(f"checkElem: {val = }")
		return "-"

def getScaleOutput(val, values):
	return str(values.get(val))[:-2]

# ===========================================================

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
			logging.warning(f"Not added to list: {i} - LINE {line}; ROW {row}; POS: {count}")
	return score

def dataToScore(input: str, line: int, row: int) -> int:
	input = str(input)
	return listToScore(dataToList(input), line, row)