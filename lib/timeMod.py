import time

def getTime():
	return str(time.time()).split(".")[0]

def timeToLocal(epoch):
	return str(time.ctime(int(epoch)))