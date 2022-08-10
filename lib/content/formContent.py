import logging

class elementContent:

	PHQ9_radio_long = ["0 - Not at all", "1 - Several days", "2 - More than half the days", "3 - Nearly every day"]
	PHQ9_radio_quick = ["0","1","2","3"]

	GAD7_radio_long = ["0 - Not at all", "1 - Several days", "2 - More than half the days", "3 - Nearly every day"]
	GAD7_radio_quick = ["0","1","2","3"]

	phobia_radio_long = ["0 - Would not avoid it", "1", "2 - Slightly avoid it", "3", "4 - Definitely avoid it", "5", "6 - Markedly avoid it", "7", "8 - Always avoid it"]
	phobia_radio_quick = ["0","1","2","3","4","5","6","7","8"]

	WSAS_radio_long = ["0 - Not at all","1","2 - Slightly","3","4 - Definitely","5","6 - Markedly","7","8 - Very severely"]
	WSAS_radio_quick = ["0","1","2","3","4","5","6","7","8"]
	
	def getRadioText(radioType = "q"):
		if radioType == "q":
			logging.debug(f"{radioType = }")
			return elementContent.PHQ9_radio_quick, elementContent.GAD7_radio_quick, elementContent.phobia_radio_quick, elementContent.WSAS_radio_quick
		elif radioType == "l":
			return elementContent.PHQ9_radio_long, elementContent.GAD7_radio_long, elementContent.phobia_radio_long, elementContent.WSAS_radio_long
		else:
			logging.error(f"getRadioText bad arg: {radioType = }")