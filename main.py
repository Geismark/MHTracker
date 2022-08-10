import logging, sys, os

from lib.timeMod import getTime
from lib.manipulateMod import getQuestionnaireOutput, dataToScore
from lib.layoutsMod import getLayouts

import csv, time
import PySimpleGUI as sg
from pathlib import Path

# =======================================
logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s]: %(message)s')
sys.dont_write_bytecode = True
version = 0.1
testing = False
# =======================================

def printScores(type=1, dataFile="base.csv"):
	directory = Path(__file__).parent.resolve()
	fileDirectory = str(directory) + "\\" + dataFile
	if not Path(fileDirectory).is_file():
		logging.error("File not found [printScores]")
		return
	with open(fileDirectory) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				# print(f'Column names are {", ".join(row)}')
				line_count += 1
			else:
				if type == 1:
					print(f'\tStart: {time.ctime(int(row[0]))}. Duration: {int(row[1]) - int(row[0])} seconds')
					hold = ["err", "err"]
					for i in [2, 3, 4, 5]:
						hold.append(dataToScore(row[i], line_count, i))
					print(f'\t\tDepression: {hold[2]}\tAnxiety: {hold[3]}\tPhobia: {hold[4]}\tW&SAS: {hold[5]}')
				elif type == 0:
					print(f'\tStart: {time.ctime(int(row[0]))}. Duration: {int(row[1]) - int(row[0])} seconds')
					print(f'\t\tDepression: {dataToScore(row[2], line_count, 2)}')
					print(f'\t\tAnxiety: -- {dataToScore(row[3], line_count, 3)}')
					print(f'\t\tPhobia: --- {dataToScore(row[4], line_count, 4)}')
					print(f'\t\tW&SAS: ---- {dataToScore(row[5], line_count, 5)}')
				line_count += 1
		print(f'******* {line_count} lines processed. *******')


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
			logging.INFO(f"{scores = }")
			window.write_event_value("Exit", "") # trigger window close
		elif event in ["-NEXT1-", "-NEXT2-", "-NEXT3-", "-NEXT4-", "-NEXT5-"]:
			window["-TABGROUP-"].Widget.select(int(event[-2]))
	window.close()
	exit(0)


	
if __name__ == "__main__":
	main()
	# printScores()