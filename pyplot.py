from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from pathlib import Path
from lib.plotMod import getPlotDatetimes
from lib.plotMod import plotRound
from pandas import read_csv as pd_read_csv

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# _VARS = {'window': False}

# https://www.youtube.com/watch?v=_LWjaAiKaf8&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=8&ab_channel=CoreySchafer

def pyPlot():
	plotOut = plt.figure()

	x_date = []
	date_hold = []
	y_PHQ9 = []
	y_GAD7 = []
	y_phobia = []
	y_WSAS = []

	directory = Path(__file__).parent.resolve()
	fileDirectory = Path(str(directory) + "\\lib\\data\\" + "base.csv")

	data = pd_read_csv(fileDirectory, index_col=None, dtype=str).reset_index(drop=True)
	date_hold = data["startDate"]
	y_PHQ9 = getScoreTotals(data["PHQ-9"])
	y_GAD7 = getScoreTotals(data["GAD-7"])
	y_phobia = getScoreTotals(data["Phobia"])
	y_WSAS = getScoreTotals(data["W&SAS"])

	x_date = getPlotDatetimes(date_hold)

	plt.plot(x_date, y_PHQ9, color="b", linestyle="-", marker="D", label="PHQ9")
	plt.plot(x_date, y_GAD7, color="g", linestyle="--", marker="v", label="GAD7")
	plt.plot(x_date, y_phobia, color="r", linestyle="-.", marker="o", label="Phobia")
	plt.plot(x_date, y_WSAS, color="m", linestyle=":", marker="^", label="W&SAS")
	# plt.xlim()
	plt.ylim(0, plotRound(max(y_PHQ9 + y_GAD7 + y_phobia + y_WSAS)))

	plt.gcf().autofmt_xdate()
	date_format = mpl_dates.DateFormatter("%d/%m/%y")
	plt.gca().xaxis.set_major_formatter(date_format)
	plt.legend()

	plt.xlabel("Time")
	plt.ylabel("Scores")
	plt.title("Questionnaire Scoring")
	# plt.grid(True)
	plt.tight_layout()

	# plt.axhline(15, linewidth=2, color="orange")

	# plt.show()
	return plotOut

def getScoreTotals(input):
	output = []
	for data in input:
		total = 0
		for val in list(str(data)):
			total += int(val)
		output.append(total)
	return output


def draw_figure(canvas, figure=pyPlot()):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


if __name__ == "__main__":
	pyPlot()

