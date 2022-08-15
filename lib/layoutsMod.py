import logging, string
import PySimpleGUI as sg
from random import randrange, choice, SystemRandom


# FUTUREDO remove excess non-lib tries needed for testing
try:
	from lib.content.questionnaireActual import FormQuestions as qu
except ImportError:
	logging.debug("Couldn't import questionnaireActual")
	try:
		from lib.content.questionnairePublic import FormQuestionsPublic as qu
	except ImportError:
		from content.questionnaireActual import FormQuestions as qu
	except Exception as ex:
		logging.critical(f"Import error: {ex = }")
try:
	from lib.content.formContent import elementContent as ec
except ImportError:
	from content.formContent import elementContent as ec

def getTestList(questions, responses, tests, isRadio=True):
	if tests==[False]:
		return [None for _ in questions]
	elif tests in [[], [True]]:
		if isRadio:
			return [randrange(0, len(responses)) for _ in questions]
		elif not isRadio:
			out = [randrange(responses[0], responses[1]) for _ in questions]
			out[-1] = [randrange(responses[2], responses[3])]
			return out
	else:
		if len(tests) != len(questions):
			logging.error(f"Manual test list length != questions length:\n\t{tests = }\n\t{questions = }\n\t{responses = }")
			return None
		logging.debug(f"{tests = }")
		return tests
	return
def getTestListCB(questions, testsCB):
	if testsCB == [False]:
		return [False for _ in questions]
	elif testsCB in [[], [True]]:
		return [choice([True, False]) for _ in questions]
	else:
		if len(testsCB) != len(questions):
			logging.error(f"Manual CB test list length != questions length:\n\t{testsCB = }\n\t{questions = }")
			return None
		return testsCB


def getRadioList(responses, group, keyBase, tests):
	out = []
	for i, text in enumerate(responses):
		out.append(sg.Radio(text, group, key=f"-{keyBase}{i}-", default=(tests==i)))
	return out

def getTabLayout(questions, fo, groupBase, keyCode, responses, tests: list, appends: list):
	lo = []
	
	tests = getTestList(questions, responses, tests)
	if tests==None:
		return [sg.Button("Exit")]

	for i, q in enumerate(questions):
		lo.append([sg.Text(q, font=fo)])
		lo.append(getRadioList(responses, f"{groupBase}{i+1}", f"{keyCode}{i+1}", tests[i]))
	
	return lo + appends
	

def getNotesTabLayout(titleSlider, questionsSlider, fo, keyBaseSlider, sliderRanges, sizeSlider, testingSlider,
						questionsCB, keyBaseCB, testingCB, questionsExtra, extraDefault, appends):
	lo = []
	
	# TODO get tests
	testsSlider = getTestList(questionsSlider, [i for i in sliderRanges], testingSlider, isRadio=False)
	testingCB = getTestListCB(questionsCB, testingCB)
	if testsSlider == None or testingCB == None:
		return [sg.Button("Exit")]
	
	lo.append([sg.Text(titleSlider)])

	for i, qu in enumerate(questionsSlider):
		if i != len(questionsSlider)-1:
			lo.append([sg.Text(qu, font=fo)])
			lo.append([sg.Slider(orientation="h", key=f"-{keyBaseSlider}{i}-", range=(sliderRanges[0], sliderRanges[1]), default_value=testsSlider[i], size=sizeSlider)])
		elif i == len(questionsSlider)-1:
			lo.append([sg.VPush()])
			lo.append([sg.Text(qu, font=fo)])
			lo.append([sg.Slider(orientation="h", key=f"-{keyBaseSlider}{i}-", range=(sliderRanges[2], sliderRanges[3]), default_value=testsSlider[i], size=sizeSlider)])
	
	CBs = []
	for i, qu in enumerate(questionsCB):
		CBs.append(sg.Checkbox(qu, key=f"-{keyBaseCB}{i}", default=testingCB[i]))
	lo.append(CBs)

	lo.append([sg.Text(questionsExtra[0])])
	lo.append([sg.Multiline(extraDefault, size=(10,1), expand_x=True, expand_y=True, k='-EXTRAS-')])
	
	return lo + appends

def getQuestionnaireLayouts(fo, radioType="q", testing=False):
	# TODO have single list for testing args

	p, g, ph, w = ec.getRadioText(radioType=radioType)

	if testing:
		extraDefault = ''.join(SystemRandom().choice(string.ascii_letters + string.punctuation + string.digits) for _ in range(40))
		extraDefault = extraDefault[:20] + "\n\t\t" + extraDefault[20:]
	else:
		extraDefault = ""

	info_layout = [
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT1-"), sg.Button("Btn")]
					]

	PHQ9_layout = getTabLayout(qu.PHQ9, fo, "PHQ9", "P", p, [True], [[sg.VPush()], [sg.Button("Next", key="-NEXT2-"), sg.Push(), sg.Button("Help")]])

	GAD7_layout = getTabLayout(qu.GAD7, fo, "GAD7", "G", g, [True], [[sg.VPush()], [sg.Button("Next", key="-NEXT3-"), sg.Push(), sg.Button("Help")]])
	
	Phobia_layout = getTabLayout(qu.phobia, fo, "Phobia", "PH", ph, [True], [[sg.VPush()], [sg.Button("Next", key="-NEXT4-"), sg.Push(), sg.Button("Help")]])
	
	WSAS_layout = getTabLayout(qu.WSAS, fo, "WSAS", "W", w, [True], [[sg.VPush()], [sg.Button("Next", key="-NEXT5-"), sg.Push(), sg.Button("Help")]])
	
	notes_layout = getNotesTabLayout(
										"In the past 7 days:", qu.slider, fo, "N", (0,7,1,10), (35,10), [True],
										qu.checkbox, "CB", [True], qu.extra, extraDefault, [[sg.Button("Submit", key="-SUBMIT-")]]
									)

	return info_layout, PHQ9_layout, GAD7_layout, Phobia_layout, WSAS_layout, notes_layout

def getMainLayouts():
	home_layout = [
					# FUTUREDO change from quick to short radio
					[sg.Button("Questionnaire", key="-QUESTIONNAIRE-"), sg.Checkbox("Use quick inputs?", key="-RADIOTYPEQUICK-")],
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT1-"), sg.Button("Btn")]
					]
	graphs_layout = [
					[sg.Canvas(key="-MAINCANVAS-")],
					[sg.VPush()],
					[sg.Button("Previous", key="-PREV0-"), sg.Button("Graphs", key="-GRAPHS-")]
					]

	return home_layout, graphs_layout


if __name__ == "__main__":
	fo = "Helvitica 12 bold underline"
	getQuestionnaireLayouts(fo)