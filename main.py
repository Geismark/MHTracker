import logging
from pyplot import draw_figure
from lib.layoutsMod import getMainLayouts
from questionnaire import questionnaireWindow
import PySimpleGUI as sg

# =======================================
logging.basicConfig(
					level = logging.DEBUG,
					datefmt = '%Y-%m-%d %H:%M:%S',
					format = '[%(levelname)s] [%(asctime)s] - [%(funcName)s]: %(message)s'
					)
version = 0.1

# FIXME logging time format
# https://stackoverflow.com/questions/3220284/how-to-customize-the-time-format-for-python-logging
# =======================================

# FUTUREDO configure default fonts, themes, etc.
def makeHomeWindow(theme="DarkGrey3"):
	sg.theme(theme)

	home_layout, graphs_layout = getMainLayouts()
	# TODO add customisation/interaction to graph

	layout = []
	layout += [
		[
			sg.TabGroup([[
				sg.Tab("Home", home_layout),
				sg.Tab("Graphs", graphs_layout)
			]],
			key="-TABGROUP-", 
			enable_events=True)
		]
	]

	# layout[-1].append(sg.Sizegrip())
	window = sg.Window('My Progress', layout, font=("Helvitica"), resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
	# window.set_min_size(window.size)
	return window

def mainWindow(testing=False):
	window = makeHomeWindow()
	draw_figure(window["-MAINCANVAS-"].TKCanvas)
	while True:
		event, values = window.read(timeout=100)
		if event in [None, "-EXIT-", "Exit"]:
			logging.info(f"Main Window EXIT")
			break
		# FUTUREDO change nexts from static to dynamic (PREVx)
		elif event in ["-NEXT0-","-NEXT1-", "-NEXT2-", "-NEXT3-", "-NEXT4-", "-NEXT5-", "-PREV0-"]:
			window["-TABGROUP-"].Widget.select(int(event[-2]))
		elif event == "-QUESTIONNAIRE-":
			if window["-RADIOTYPEQUICK-"].get():
				radioType = "q"
			else:
				radioType = "l"
			questionnaireWindow(radioType=radioType, testing=testing)
	window.close()
	exit(0)


if __name__ == "__main__":
	mainWindow(testing=True)