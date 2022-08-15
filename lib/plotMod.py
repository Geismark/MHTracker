from lib.timeMod import epochToPlotDate

def plotRound(x, base=5):
    return base * (((x)//base)+1)

def getPlotDatetimes(dates):
	output = []
	for val in dates:
		output.append(epochToPlotDate(val))
	return output