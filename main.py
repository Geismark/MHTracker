import logging, sys, os

from lib.timeMod import getTime
from lib.manipulateMod import getQuestionnaireOutput
from lib.layoutsMod import getLayouts

import PySimpleGUI as sg

# =======================================
logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s]: %(message)s') # can add time if desired
sys.dont_write_bytecode = True
version = 0.1
testing = False
# =======================================

def makeQuestionWindow(theme="DarkGrey3", radioType="q"):
	fo = "Helvitica 12 bold underline"
	sg.theme(theme)

	info_layout, PHQ9_layout, GAD7_layout, Phobia_layout, WSAS_layout, notes_layout = getLayouts(fo=fo, radioType=radioType, testing=testing)

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
	window = sg.Window('My Progress', layout, font=("Helvitica"), resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
	# window.set_min_size(window.size)
	return window

def main():
	window = makeQuestionWindow(radioType="l")
	startTime = getTime()
	while True:
		event, values = window.read(timeout=100)
		if event in (None, 'Exit'):
			logging.info(f"Window EXIT")
			break
		elif event == "-SUBMIT-":
			scores = getQuestionnaireOutput(values)
			logging.info(f"{scores = }")
			window.write_event_value("Exit", "") # trigger window close
		elif event in ["-NEXT1-", "-NEXT2-", "-NEXT3-", "-NEXT4-", "-NEXT5-"]:
			window["-TABGROUP-"].Widget.select(int(event[-2]))
	window.close()
	exit(0)


if __name__ == "__main__":
	testing = True
	main()
	# printScores()