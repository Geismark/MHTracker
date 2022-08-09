import logging
from turtle import getshapes
logging.basicConfig(level = logging.INFO, format = '[%(levelname)s]: %(message)s')

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
			print(f"ERROR questionnaire input scoring: {i} @ {count}\n\t{inputs}")
	output = [PHQ, GAD, phobia, WSAS]
	return output

def getQuestionnaireOutput(values:list) -> list:
	logging.debug("gQS test")
	output = []
	PHQ = "---------"
	GAD = "-------"
	phobia = "---"
	WSAS = "-----"
	scales = "------" # last of notes is 0-9, questionnaire is 1-10
	checks = "-----"
	extra = ""

	# switch case?
	for val, count in enumerate(values):
		if val[1] == "P":
			if val[2] == "H":
				phobia = stringChar(phobia, val[4], val[3])
			else:
				PHQ = stringChar(PHQ, val[3], val[2])
				pass
		elif val[1] == "G":
			GAD = stringChar(GAD, val[3], val[2])
		elif val[1] == "W":
			WSAS = stringChar(WSAS, val[3], val[2])
		elif val[1] == "N": # sliders, 0-9 rather than 1-10
			if val[2] == "6":
				scales = stringChar(scales, str(int(getScaleOutput(val, values))-1), val[2])
			else:
				scales = stringChar(scales, getScaleOutput(val, values), val[2])
		elif val[1:2] == "CB": # checkboxes
			checks = stringChar(checks, checkElem(val, values), val[3])
		elif val == "-EXTRAS-": # textbox
			extra = values.get(val)
		

	return output

def stringChar(str, char, pos):
	"""
	pos start @ 0
	"""
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
	return values.get(val)[:-2]