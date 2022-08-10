import logging, time, csv
from manipulateMod import dataToScore
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