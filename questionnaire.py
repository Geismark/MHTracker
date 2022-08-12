import logging
from lib.timeMod import getTime
from lib.manipulateMod import getQuestionnaireOutput
from lib.layoutsMod import getQuestionnaireLayouts
from lib.outputMod import saveDataOutput
import PySimpleGUI as sg

# =======================================
logging.basicConfig(
					level = logging.DEBUG,
					datefmt = '%Y-%m-%d %H:%M:%S',
					format = '[%(levelname)s] [%(asctime)s] - [%(funcName)s]: %(message)s'
					)
# =======================================

def makeQuestionWindow(theme="DarkGrey3", radioType="q", testing=False):
	fo = "Helvitica 12 bold underline"
	sg.theme(theme)

	info_layout, PHQ9_layout, GAD7_layout, Phobia_layout, WSAS_layout, notes_layout = getQuestionnaireLayouts(fo=fo, radioType=radioType, testing=testing)

	layout = []
	layout += [
		[
			sg.TabGroup([[
				sg.Tab("Info", info_layout),
				sg.Tab("PHQ-9", PHQ9_layout),
				sg.Tab("GAD-7", GAD7_layout),
				sg.Tab("Phobia", Phobia_layout),
				sg.Tab("W&SAS", WSAS_layout),
				sg.Tab("Notes", notes_layout)
			]],
			key="-TABGROUP-", 
			enable_events=True)
		]
	]

	# layout[-1].append(sg.Sizegrip())
	window = sg.Window('Questionnaire', layout, font=("Helvitica"), resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
	# window.set_min_size(window.size)
	return window

# FUTUREDO questionnaire info
# FUTUREDO questionnaire help buttons

def questionnaireWindow(radioType="l", testing=False):
	window = makeQuestionWindow(radioType=radioType, testing=testing)
	startTime = getTime()
	while True:
		event, values = window.read(timeout=100)
		if event in (None, 'Exit'):
			logging.info(f"Questionnaire Window EXIT")
			break
		elif event in ["-SUBMIT-", "Btn"]:
			scores = getQuestionnaireOutput(values)
			saveDataOutput(scores, startTime)
			window.write_event_value("Exit", "") # trigger window close
		elif event in ["-NEXT0-", "-NEXT1-", "-NEXT2-", "-NEXT3-", "-NEXT4-", "-NEXT5-"]:
			window["-TABGROUP-"].Widget.select(int(event[-2]))
	window.close()
	exit(0)


if __name__ == "__main__":
	testing = True
	questionnaireWindow(radioType="l", testing=testing)
	# printScores()