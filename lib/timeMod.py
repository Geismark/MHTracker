import time
from datetime import datetime

def getTime():
	return str(time.time()).split(".")[0]

def timeToLocal(epoch):
	return str(time.ctime(int(epoch)))

def epochToPlotDate(epoch):
	output = []
	# FIXME https://www.programiz.com/python-programming/datetime/timestamp-datetime
	# FIXME datetime.datetime.fromtimestamp
	t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(int(epoch)))
	t = t.split("-")
	d = [int(val) for val in t]
	return datetime(d[0], d[1], d[2], d[3], d[4], d[5])