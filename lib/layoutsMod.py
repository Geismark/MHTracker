import PySimpleGUI as sg


def getRadioText(radioType = "q"):
	listOutput = []

	PHQ9_radio_long = ["0 - Not at all", "1 - Several days", "2 - More than half the days", "3 - Nearly every day"]
	PHQ9_radio_quick = ["0","1","2","3"]

	GAD7_radio_long = ["0 - Not at all", "1 - Several days", "2 - More than half the days", "3 - Nearly every day"]
	GAD7_radio_quick = ["0","1","2","3"]

	Phobia_radio_long = ["0 - Would not avoid it", "1", "2 - Slightly avoid it", "3", "4 - Definitely avoid it", "5", "6 - Markedly avoid it", "7", "8 - Always avoid it"]
	Phobia_radio_quick = ["0","1","2","3","4","5","6","7","8"]

	WSAS_radio_long = ["0 - Not at all","1","2 - Slightly","3","4 - Definitely","5","6 - Markedly","7","8 - Very severely"]
	WSAS_radio_quick = ["0","1","2","3","4","5","6","7","8"]

	if radioType == "q":
		listOutput.extend((PHQ9_radio_quick, GAD7_radio_quick, Phobia_radio_quick, WSAS_radio_quick))
	elif radioType == "l":
		listOutput.extend((PHQ9_radio_long, GAD7_radio_long, Phobia_radio_long, WSAS_radio_long))
	else:
		"ERROR: radio select type"

	return listOutput

def getLayouts(fo, radioType="q", testing=False):

	radioTexts = getRadioText(radioType)
	p = radioTexts[0]
	g = radioTexts[1]
	ph = radioTexts[2]
	w = radioTexts[3]

	info_layout = [
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT1-"), sg.Button("Btn")]
					]

	PHQ9_layout = [
					[sg.Text("1. Little interest or pleasure in doing things", font=fo)],
					[sg.Radio(p[0], "PHQ91", k='-P10-', default=testing),sg.Radio(p[1], "PHQ91", k='-P11-'),sg.Radio(p[2], "PHQ91", k='-P12-'),sg.Radio(p[3], "PHQ91", k='-P13-')],
					[sg.Text("2. Feeling down, depressed or hopeless", font=fo)],
					[sg.Radio(p[0], "PHQ92", k='-P20-', default=testing),sg.Radio(p[1], "PHQ92", k='-P21-'),sg.Radio(p[2], "PHQ92", k='-P22-'),sg.Radio(p[3], "PHQ92", k='-P23-')],
					[sg.Text("3. Trouble falling, or staying asleep or sleeping too much", font=fo)],
					[sg.Radio(p[0], "PHQ93", k='-P30-'),sg.Radio(p[1], "PHQ93", k='-P31-', default=testing),sg.Radio(p[2], "PHQ93", k='-P32-'),sg.Radio(p[3], "PHQ93", k='-P33-')],
					[sg.Text("4. Feeling tired or having little energy", font=fo)],
					[sg.Radio(p[0], "PHQ94", k='-P40-'),sg.Radio(p[1], "PHQ94", k='-P41-', default=testing),sg.Radio(p[2], "PHQ94", k='-P42-'),sg.Radio(p[3], "PHQ94", k='-P43-')],
					[sg.Text("5. Poor appetite or overeating", font=fo)],
					[sg.Radio(p[0], "PHQ95", k='-P50-'),sg.Radio(p[1], "PHQ95", k='-P51-'),sg.Radio(p[2], "PHQ95", k='-P52-', default=testing),sg.Radio(p[3], "PHQ95", k='-P53-')],
					[sg.Text("6. Feeling bad about yourself - or that you are a failure or have let yourself or your family down", font=fo)],
					[sg.Radio(p[0], "PHQ96", k='-P60-'),sg.Radio(p[1], "PHQ96", k='-P61-'),sg.Radio(p[2], "PHQ96", k='-P62-', default=testing),sg.Radio(p[3], "PHQ96", k='-P63-')],
					[sg.Text("7. Trouble concentrating on things, such as reading the newspaper or watching television", font=fo)],
					[sg.Radio(p[0], "PHQ97", k='-P70-'),sg.Radio(p[1], "PHQ97", k='-P71-'),sg.Radio(p[2], "PHQ97", k='-P72-'),sg.Radio(p[3], "PHQ97", k='-P73-', default=testing)],
					[sg.Text("8. Moving or speaking so slowly that other people could have noticed?\n\tOr the opposite - being so fidgety or restless that you have been moving around a lot more than usual", font=fo)],
					[sg.Radio(p[0], "PHQ98", k='-P80-'),sg.Radio(p[1], "PHQ98", k='-P81-'),sg.Radio(p[2], "PHQ98", k='-P82-'),sg.Radio(p[3], "PHQ98", k='-P83-', default=testing)],
					[sg.Text("9. Thoughts that you would be better off dead or of hurting yourself in some way", font=fo)],
					[sg.Radio(p[0], "PHQ99", k='-P90-', default=testing),sg.Radio(p[1], "PHQ99", k='-P91-'),sg.Radio(p[2], "PHQ99", k='-P92-'),sg.Radio(p[3], "PHQ99", k='-P93-')],
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT2-"), sg.Push(), sg.Button("Help")]
					]

	GAD7_layout = [
					[sg.Text("1. Feeling nervous, anxious or on edge", font=fo)],
					[sg.Radio(g[0], "GAD71", k='-G10-', default=testing),sg.Radio(g[1], "GAD71", k='-G11-'),sg.Radio(g[2], "GAD71", k='-G12-'),sg.Radio(g[3], "GAD71", k='-G13-')],
					[sg.Text("2. Not being able to stop or control worrying", font=fo)],
					[sg.Radio(g[0], "GAD72", k='-G20-', default=testing),sg.Radio(g[1], "GAD72", k='-G21-'),sg.Radio(g[2], "GAD72", k='-G22-'),sg.Radio(g[3], "GAD72", k='-G23-')],
					[sg.Text("3. Worring too much about different things", font=fo)],
					[sg.Radio(g[0], "GAD73", k='-G30-'),sg.Radio(g[1], "GAD73", k='-G31-', default=testing),sg.Radio(g[2], "GAD73", k='-G32-'),sg.Radio(g[3], "GAD73", k='-G33-')],
					[sg.Text("4. Trouble relaxing", font=fo)],
					[sg.Radio(g[0], "GAD74", k='-G40-'),sg.Radio(g[1], "GAD74", k='-G41-', default=testing),sg.Radio(g[2], "GAD74", k='-G42-'),sg.Radio(g[3], "GAD74", k='-G43-')],
					[sg.Text("5. Being so restless that it is hard to sit still", font=fo)],
					[sg.Radio(g[0], "GAD75", k='-G50-'),sg.Radio(g[1], "GAD75", k='-G51-'),sg.Radio(g[2], "GAD75", k='-G52-', default=testing),sg.Radio(g[3], "GAD75", k='-G53-')],
					[sg.Text("6. Becoming easily annoyed or irritable", font=fo)],
					[sg.Radio(g[0], "GAD76", k='-G60-'),sg.Radio(g[1], "GAD76", k='-G61-'),sg.Radio(g[2], "GAD76", k='-G62-', default=testing),sg.Radio(g[3], "GAD76", k='-G63-')],
					[sg.Text("7. Feeling afraid as if something awful might happen", font=fo)],
					[sg.Radio(g[0], "GAD77", k='-G70-'),sg.Radio(g[1], "GAD77", k='-G71-'),sg.Radio(g[2], "GAD77", k='-G72-'),sg.Radio(g[3], "GAD77", k='-G73-', default=testing)],
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT3-"), sg.Push(), sg.Button("Help")]
					]
	
	Phobia_layout = [
					[sg.Text("1. Social situations due to a fear of being embarrassed or making a fool of myself", font=fo)],
					[sg.Radio(ph[0], "Phobia1", k='-PH10-', default=testing),sg.Radio(ph[1], "Phobia1", k='-PH11-'),sg.Radio(ph[2], "Phobia1", k='-PH12-'),sg.Radio(ph[3], "Phobia1", k='-PH13-'),sg.Radio(ph[4], "Phobia1", k='-PH14-'),sg.Radio(ph[5], "Phobia1", k='-PH15-'),sg.Radio(ph[6], "Phobia1", k='-PH16-'),sg.Radio(ph[7], "Phobia1", k='-PH17-'),sg.Radio(ph[8], "Phobia1", k='-PH18-')],
					[sg.Text("2. Certain situations because of a fear of having a panic attack or other distressing symptoms\n\t(such as loss of bladder control, vomiting or dizziness)", font=fo)],
					[sg.Radio(ph[0], "Phobia2", k='-PH20-'),sg.Radio(ph[1], "Phobia2", k='-PH21-'),sg.Radio(ph[2], "Phobia2", k='-PH22-'),sg.Radio(ph[3], "Phobia2", k='-PH23-'),sg.Radio(ph[4], "Phobia2", k='-PH24-'),sg.Radio(ph[5], "Phobia2", k='-PH25-'),sg.Radio(ph[6], "Phobia2", k='-PH26-', default=testing),sg.Radio(ph[7], "Phobia2", k='-PH27-'),sg.Radio(ph[8], "Phobia2", k='-PH28-')],
					[sg.Text("3. Certain situations because of a fear of particular objects or activities\n\t(such as animals, heights, seeing blood, being in confined spaces, driving or flying)", font=fo)],
					[sg.Radio(ph[0], "Phobia3", k='-PH30-'),sg.Radio(ph[1], "Phobia3", k='-PH31-'),sg.Radio(ph[2], "Phobia3", k='-PH32-'),sg.Radio(ph[3], "Phobia3", k='-PH33-', default=testing),sg.Radio(ph[4], "Phobia3", k='-PH34-'),sg.Radio(ph[5], "Phobia3", k='-PH35-'),sg.Radio(ph[6], "Phobia3", k='-PH36-'),sg.Radio(ph[7], "Phobia3", k='-PH37-'),sg.Radio(ph[8], "Phobia3", k='-PH38-')],
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT4-"), sg.Push(), sg.Button("Help")]
					]
	
	WSAS_layout = [
					[sg.Text("1. Work - if you are retired or choose not to have a job for reasons unrelated to your problem, please select N/A (not applicable)", font=fo)],
					[sg.Radio(w[0], "WSAS1", k='-W10-', default=testing),sg.Radio(w[1], "WSAS1", k='-W11-'),sg.Radio(w[2], "WSAS1", k='-W12-'),sg.Radio(w[3], "WSAS1", k='-W13-'),sg.Radio(w[4], "WSAS1", k='-W14-'),sg.Radio(w[5], "WSAS1", k='-W15-'),sg.Radio(w[6], "WSAS1", k='-W16-'),sg.Radio(w[7], "WSAS1", k='-W17-'),sg.Radio(w[8], "WSAS1", k='-W18-')],
					[sg.Text("2. Home management - cleaning, tidying, shopping, cooking, looking after home/children, paying bills etc", font=fo)],
					[sg.Radio(w[0], "WSAS2", k='-W20-'),sg.Radio(w[1], "WSAS2", k='-W21-'),sg.Radio(w[2], "WSAS2", k='-W22-', default=testing),sg.Radio(w[3], "WSAS2", k='-W23-'),sg.Radio(w[4], "WSAS2", k='-W24-'),sg.Radio(w[5], "WSAS2", k='-W25-'),sg.Radio(w[6], "WSAS2", k='-W26-'),sg.Radio(w[7], "WSAS2", k='-W27-'),sg.Radio(w[8], "WSAS2", k='-W28-')],
					[sg.Text("3. Social leisure activities - with other people, e.g. parties, pubs, outings, entertaining etc", font=fo)],
					[sg.Radio(w[0], "WSAS3", k='-W30-'),sg.Radio(w[1], "WSAS3", k='-W31-'),sg.Radio(w[2], "WSAS3", k='-W32-'),sg.Radio(w[3], "WSAS3", k='-W33-'),sg.Radio(w[4], "WSAS3", k='-W34-', default=testing),sg.Radio(w[5], "WSAS3", k='-W35-'),sg.Radio(w[6], "WSAS3", k='-W36-'),sg.Radio(w[7], "WSAS3", k='-W37-'),sg.Radio(w[8], "WSAS3", k='-W38-')],
					[sg.Text("4. Private leisure activities - done alone, e.g. reading, gardening, sewing, hobbies, walking etc", font=fo)],
					[sg.Radio(w[0], "WSAS4", k='-W40-'),sg.Radio(w[1], "WSAS4", k='-W41-'),sg.Radio(w[2], "WSAS4", k='-W42-'),sg.Radio(w[3], "WSAS4", k='-W43-'),sg.Radio(w[4], "WSAS4", k='-W44-'),sg.Radio(w[5], "WSAS4", k='-W45-'),sg.Radio(w[6], "WSAS4", k='-W46-', default=testing),sg.Radio(w[7], "WSAS4", k='-W47-'),sg.Radio(w[8], "WSAS4", k='-W48-')],
					[sg.Text("5. Family and relationships - form and maintain close relationships with others including the people that I live with", font=fo)],
					[sg.Radio(w[0], "WSAS5", k='-W50-'),sg.Radio(w[1], "WSAS5", k='-W51-'),sg.Radio(w[2], "WSAS5", k='-W52-'),sg.Radio(w[3], "WSAS5", k='-W53-'),sg.Radio(w[4], "WSAS5", k='-W54-'),sg.Radio(w[5], "WSAS5", k='-W55-'),sg.Radio(w[6], "WSAS5", k='-W56-'),sg.Radio(w[7], "WSAS5", k='-W57-'),sg.Radio(w[8], "WSAS5", k='-W58-', default=testing)],
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT5-"), sg.Push(), sg.Button("Help")]
					]
	
	notes_layout = [
		[sg.Text("In the past 7 days:")],
					[sg.Text("1. How many days did you go outside", font=fo)],
					[sg.Slider(orientation='h', key='-N0-', range=(0,7), default_value=0, size=(35,10))],
					[sg.Text("2. How many days did you partake in active physical exercise", font=fo)],
					[sg.Slider(orientation='h', key='-N1-', range=(0,7), default_value=0, size=(35,10))],
					[sg.Text("3. How many days did you talk with anybody face to face", font=fo)],
					[sg.Slider(orientation='h', key='-N2-', range=(0,7), default_value=0, size=(35,10))],
					[sg.Text("4. How many days did you talk with friends", font=fo)],
					[sg.Slider(orientation='h', key='-N3-', range=(0,7), default_value=0, size=(35,10))],
					[sg.Text("5. How many days did you talk with family", font=fo)],
					[sg.Slider(orientation='h', key='-N4-', range=(0,7), default_value=0, size=(35,10))],
                	[sg.VPush()],
					[sg.Text("6. Rate your week out of 10", font=fo)],
					[sg.Slider(orientation='h', key='-N5-', range=(1,10), default_value=0, size=(35,10))],
					[sg.Checkbox('Hobbies', default=testing, k='-CB0-'),
						sg.Checkbox('Work', default=False, k='-CB1-'),
						sg.Checkbox('Revising', default=testing, k='-CB2-'),
						sg.Checkbox('Test', default=False, k='-CB3-'),
						sg.Checkbox('Exam', default=testing, k='-CB4-')],
					[sg.Text("Anything else you'd like to say about the time since you last completed this questionnaire:")],
					[sg.Multiline('', size=(10,1), expand_x=True, expand_y=True, k='-EXTRAS-')],
					[sg.Button("Submit", key="-SUBMIT-")]
					]

	return info_layout, PHQ9_layout, GAD7_layout, Phobia_layout, WSAS_layout, notes_layout