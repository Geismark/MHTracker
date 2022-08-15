import logging, time, csv, re
from lib.timeMod import getTime
from lib.manipulateMod import dataToScore
from pathlib import Path


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

def saveDataOutput(data, startTime, dataFileName="base.csv", dataFileDir=None):
	# FUTUREDO future functionality for multiple files?
	# data = ['001122330', '0011223', '063', '02468', '000000', '10101', 'abc\n123\ndefghi\n\t456789']
	
	if dataFileDir:
		directory = dataFileDir
	else:
		directory = Path(__file__).parent.resolve()
		directory = Path(str(directory) + "\\data\\" + dataFileName)

	# TODO have backup dump file so data still saved when file not found
	if Path(directory).is_file():
		data = formatData(data, startTime)
		with open(directory, "a", newline="") as file:
			try:
				writer = csv.writer(file)
				writer.writerow(data)
			except:
				logging.critical("saveDataOutput writer failed: {directory = }\n\t{data = }")
				return False
			finally:
				file.close()
			
		return True
	else:
		logging.error(f"Directory not a file: {directory = }\n\t{data = }")
		return False

def formatData(data, startTime):
	endTime = getTime()
	data = [startTime, endTime] + data
	logging.debug(f"{data = }")

	# FIXME better way to do this!
	data[-1] = re.sub("\n", f"{{~n}}", data[-1])
	data[-1] = re.sub("\t", f"{{~t}}", data[-1])
	data[-1] = re.sub("\r", f"{{~r}}", data[-1])

	# TODO figure out how to 'fix' escape characters in strings, and why output is not in double quotes

	# Why is this needed? What causes the loss of ""?
	# csv strings SHOULD be wrapped in double-quotations to handle commas
		# how to handle comma+quotation manipulation in textbox?? re?
			# potential WRITER already handles edge cases?
	data[-1] = '"' + data[-1] + '"'

	return data