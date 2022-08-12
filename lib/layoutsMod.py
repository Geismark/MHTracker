import logging
import PySimpleGUI as sg

try:
	from lib.content.questionnaireActual import FormQuestions as qu
except ImportError:
	logging.debug("Couldn't import questionnaireActual")
	from lib.content.questionnairePublic import FormQuestionsPublic as qu
from lib.content.formContent import elementContent as ec


def getQuestionnaireLayouts(fo, radioType="q", testing=False):

	p, g, ph, w = ec.getRadioText(radioType=radioType)

	if testing:
		multilineDefault = "abc\n123\ndefghi\n\t456789"
	else:
		multilineDefault = ""

	info_layout = [
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT1-"), sg.Button("Btn")]
					]

	PHQ9_layout = [
					[sg.Text(qu.PHQ9[0], font=fo)],
					[sg.Radio(p[0], "PHQ91", k='-P10-', default=testing),sg.Radio(p[1], "PHQ91", k='-P11-'),sg.Radio(p[2], "PHQ91", k='-P12-'),sg.Radio(p[3], "PHQ91", k='-P13-')],
					[sg.Text(qu.PHQ9[1], font=fo)],
					[sg.Radio(p[0], "PHQ92", k='-P20-', default=testing),sg.Radio(p[1], "PHQ92", k='-P21-'),sg.Radio(p[2], "PHQ92", k='-P22-'),sg.Radio(p[3], "PHQ92", k='-P23-')],
					[sg.Text(qu.PHQ9[2], font=fo)],
					[sg.Radio(p[0], "PHQ93", k='-P30-'),sg.Radio(p[1], "PHQ93", k='-P31-', default=testing),sg.Radio(p[2], "PHQ93", k='-P32-'),sg.Radio(p[3], "PHQ93", k='-P33-')],
					[sg.Text(qu.PHQ9[3], font=fo)],
					[sg.Radio(p[0], "PHQ94", k='-P40-'),sg.Radio(p[1], "PHQ94", k='-P41-', default=testing),sg.Radio(p[2], "PHQ94", k='-P42-'),sg.Radio(p[3], "PHQ94", k='-P43-')],
					[sg.Text(qu.PHQ9[4], font=fo)],
					[sg.Radio(p[0], "PHQ95", k='-P50-'),sg.Radio(p[1], "PHQ95", k='-P51-'),sg.Radio(p[2], "PHQ95", k='-P52-', default=testing),sg.Radio(p[3], "PHQ95", k='-P53-')],
					[sg.Text(qu.PHQ9[5], font=fo)],
					[sg.Radio(p[0], "PHQ96", k='-P60-'),sg.Radio(p[1], "PHQ96", k='-P61-'),sg.Radio(p[2], "PHQ96", k='-P62-', default=testing),sg.Radio(p[3], "PHQ96", k='-P63-')],
					[sg.Text(qu.PHQ9[6], font=fo)],
					[sg.Radio(p[0], "PHQ97", k='-P70-'),sg.Radio(p[1], "PHQ97", k='-P71-'),sg.Radio(p[2], "PHQ97", k='-P72-'),sg.Radio(p[3], "PHQ97", k='-P73-', default=testing)],
					[sg.Text(qu.PHQ9[7], font=fo)],
					[sg.Radio(p[0], "PHQ98", k='-P80-'),sg.Radio(p[1], "PHQ98", k='-P81-'),sg.Radio(p[2], "PHQ98", k='-P82-'),sg.Radio(p[3], "PHQ98", k='-P83-', default=testing)],
					[sg.Text(qu.PHQ9[8], font=fo)],
					[sg.Radio(p[0], "PHQ99", k='-P90-', default=testing),sg.Radio(p[1], "PHQ99", k='-P91-'),sg.Radio(p[2], "PHQ99", k='-P92-'),sg.Radio(p[3], "PHQ99", k='-P93-')],
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT2-"), sg.Push(), sg.Button("Help")]
					]

	GAD7_layout = [
					[sg.Text(qu.GAD7[0], font=fo)],
					[sg.Radio(g[0], "GAD71", k='-G10-', default=testing),sg.Radio(g[1], "GAD71", k='-G11-'),sg.Radio(g[2], "GAD71", k='-G12-'),sg.Radio(g[3], "GAD71", k='-G13-')],
					[sg.Text(qu.GAD7[1], font=fo)],
					[sg.Radio(g[0], "GAD72", k='-G20-', default=testing),sg.Radio(g[1], "GAD72", k='-G21-'),sg.Radio(g[2], "GAD72", k='-G22-'),sg.Radio(g[3], "GAD72", k='-G23-')],
					[sg.Text(qu.GAD7[2], font=fo)],
					[sg.Radio(g[0], "GAD73", k='-G30-'),sg.Radio(g[1], "GAD73", k='-G31-', default=testing),sg.Radio(g[2], "GAD73", k='-G32-'),sg.Radio(g[3], "GAD73", k='-G33-')],
					[sg.Text(qu.GAD7[3], font=fo)],
					[sg.Radio(g[0], "GAD74", k='-G40-'),sg.Radio(g[1], "GAD74", k='-G41-', default=testing),sg.Radio(g[2], "GAD74", k='-G42-'),sg.Radio(g[3], "GAD74", k='-G43-')],
					[sg.Text(qu.GAD7[4], font=fo)],
					[sg.Radio(g[0], "GAD75", k='-G50-'),sg.Radio(g[1], "GAD75", k='-G51-'),sg.Radio(g[2], "GAD75", k='-G52-', default=testing),sg.Radio(g[3], "GAD75", k='-G53-')],
					[sg.Text(qu.GAD7[5], font=fo)],
					[sg.Radio(g[0], "GAD76", k='-G60-'),sg.Radio(g[1], "GAD76", k='-G61-'),sg.Radio(g[2], "GAD76", k='-G62-', default=testing),sg.Radio(g[3], "GAD76", k='-G63-')],
					[sg.Text(qu.GAD7[6], font=fo)],
					[sg.Radio(g[0], "GAD77", k='-G70-'),sg.Radio(g[1], "GAD77", k='-G71-'),sg.Radio(g[2], "GAD77", k='-G72-'),sg.Radio(g[3], "GAD77", k='-G73-', default=testing)],
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT3-"), sg.Push(), sg.Button("Help")]
					]
	
	Phobia_layout = [
					[sg.Text(qu.phobia[0], font=fo)],
					[sg.Radio(ph[0], "Phobia1", k='-PH10-', default=testing),sg.Radio(ph[1], "Phobia1", k='-PH11-'),sg.Radio(ph[2], "Phobia1", k='-PH12-'),sg.Radio(ph[3], "Phobia1", k='-PH13-'),sg.Radio(ph[4], "Phobia1", k='-PH14-'),sg.Radio(ph[5], "Phobia1", k='-PH15-'),sg.Radio(ph[6], "Phobia1", k='-PH16-'),sg.Radio(ph[7], "Phobia1", k='-PH17-'),sg.Radio(ph[8], "Phobia1", k='-PH18-')],
					[sg.Text(qu.phobia[1], font=fo)],
					[sg.Radio(ph[0], "Phobia2", k='-PH20-'),sg.Radio(ph[1], "Phobia2", k='-PH21-'),sg.Radio(ph[2], "Phobia2", k='-PH22-'),sg.Radio(ph[3], "Phobia2", k='-PH23-'),sg.Radio(ph[4], "Phobia2", k='-PH24-'),sg.Radio(ph[5], "Phobia2", k='-PH25-'),sg.Radio(ph[6], "Phobia2", k='-PH26-', default=testing),sg.Radio(ph[7], "Phobia2", k='-PH27-'),sg.Radio(ph[8], "Phobia2", k='-PH28-')],
					[sg.Text(qu.phobia[2], font=fo)],
					[sg.Radio(ph[0], "Phobia3", k='-PH30-'),sg.Radio(ph[1], "Phobia3", k='-PH31-'),sg.Radio(ph[2], "Phobia3", k='-PH32-'),sg.Radio(ph[3], "Phobia3", k='-PH33-', default=testing),sg.Radio(ph[4], "Phobia3", k='-PH34-'),sg.Radio(ph[5], "Phobia3", k='-PH35-'),sg.Radio(ph[6], "Phobia3", k='-PH36-'),sg.Radio(ph[7], "Phobia3", k='-PH37-'),sg.Radio(ph[8], "Phobia3", k='-PH38-')],
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT4-"), sg.Push(), sg.Button("Help")]
					]
	
	WSAS_layout = [
					[sg.Text(qu.WSAS[0], font=fo)],
					[sg.Radio(w[0], "WSAS1", k='-W10-', default=testing),sg.Radio(w[1], "WSAS1", k='-W11-'),sg.Radio(w[2], "WSAS1", k='-W12-'),sg.Radio(w[3], "WSAS1", k='-W13-'),sg.Radio(w[4], "WSAS1", k='-W14-'),sg.Radio(w[5], "WSAS1", k='-W15-'),sg.Radio(w[6], "WSAS1", k='-W16-'),sg.Radio(w[7], "WSAS1", k='-W17-'),sg.Radio(w[8], "WSAS1", k='-W18-')],
					[sg.Text(qu.WSAS[1], font=fo)],
					[sg.Radio(w[0], "WSAS2", k='-W20-'),sg.Radio(w[1], "WSAS2", k='-W21-'),sg.Radio(w[2], "WSAS2", k='-W22-', default=testing),sg.Radio(w[3], "WSAS2", k='-W23-'),sg.Radio(w[4], "WSAS2", k='-W24-'),sg.Radio(w[5], "WSAS2", k='-W25-'),sg.Radio(w[6], "WSAS2", k='-W26-'),sg.Radio(w[7], "WSAS2", k='-W27-'),sg.Radio(w[8], "WSAS2", k='-W28-')],
					[sg.Text(qu.WSAS[2], font=fo)],
					[sg.Radio(w[0], "WSAS3", k='-W30-'),sg.Radio(w[1], "WSAS3", k='-W31-'),sg.Radio(w[2], "WSAS3", k='-W32-'),sg.Radio(w[3], "WSAS3", k='-W33-'),sg.Radio(w[4], "WSAS3", k='-W34-', default=testing),sg.Radio(w[5], "WSAS3", k='-W35-'),sg.Radio(w[6], "WSAS3", k='-W36-'),sg.Radio(w[7], "WSAS3", k='-W37-'),sg.Radio(w[8], "WSAS3", k='-W38-')],
					[sg.Text(qu.WSAS[3], font=fo)],
					[sg.Radio(w[0], "WSAS4", k='-W40-'),sg.Radio(w[1], "WSAS4", k='-W41-'),sg.Radio(w[2], "WSAS4", k='-W42-'),sg.Radio(w[3], "WSAS4", k='-W43-'),sg.Radio(w[4], "WSAS4", k='-W44-'),sg.Radio(w[5], "WSAS4", k='-W45-'),sg.Radio(w[6], "WSAS4", k='-W46-', default=testing),sg.Radio(w[7], "WSAS4", k='-W47-'),sg.Radio(w[8], "WSAS4", k='-W48-')],
					[sg.Text(qu.WSAS[4], font=fo)],
					[sg.Radio(w[0], "WSAS5", k='-W50-'),sg.Radio(w[1], "WSAS5", k='-W51-'),sg.Radio(w[2], "WSAS5", k='-W52-'),sg.Radio(w[3], "WSAS5", k='-W53-'),sg.Radio(w[4], "WSAS5", k='-W54-'),sg.Radio(w[5], "WSAS5", k='-W55-'),sg.Radio(w[6], "WSAS5", k='-W56-'),sg.Radio(w[7], "WSAS5", k='-W57-'),sg.Radio(w[8], "WSAS5", k='-W58-', default=testing)],
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT5-"), sg.Push(), sg.Button("Help")]
					]
	
	notes_layout = [
					[sg.Text("In the past 7 days:")],
					[sg.Text(qu.slider[0], font=fo)],
					[sg.Slider(orientation='h', key='-N0-', range=(0,7), default_value=0, size=(35,10))],
					[sg.Text(qu.slider[1], font=fo)],
					[sg.Slider(orientation='h', key='-N1-', range=(0,7), default_value=0, size=(35,10))],
					[sg.Text(qu.slider[2], font=fo)],
					[sg.Slider(orientation='h', key='-N2-', range=(0,7), default_value=0, size=(35,10))],
					[sg.Text(qu.slider[3], font=fo)],
					[sg.Slider(orientation='h', key='-N3-', range=(0,7), default_value=0, size=(35,10))],
					[sg.Text(qu.slider[4], font=fo)],
					[sg.Slider(orientation='h', key='-N4-', range=(0,7), default_value=0, size=(35,10))],
                	[sg.VPush()],
					[sg.Text(qu.slider[5], font=fo)],
					[sg.Slider(orientation='h', key='-N5-', range=(1,10), default_value=0, size=(35,10))],
					[sg.Checkbox(qu.checkbox[0], default=testing, k='-CB0-'),
						sg.Checkbox(qu.checkbox[1], default=False, k='-CB1-'),
						sg.Checkbox(qu.checkbox[2], default=testing, k='-CB2-'),
						sg.Checkbox(qu.checkbox[3], default=False, k='-CB3-'),
						sg.Checkbox(qu.checkbox[4], default=testing, k='-CB4-')],
					[sg.Text(qu.extra[0])],
					[sg.Multiline(multilineDefault, size=(10,1), expand_x=True, expand_y=True, k='-EXTRAS-')],
					[sg.Button("Submit", key="-SUBMIT-")]
					]

	return info_layout, PHQ9_layout, GAD7_layout, Phobia_layout, WSAS_layout, notes_layout

def getMainLayouts():
	home_layout = [
					# FUTUREDO change from quick to short radio
					[sg.Button("Questionnaire", key="-QUESTIONNAIRE-"), sg.checkbox("Use quick inputs?", key="-RADIOTYPEQUICK-")]
					[sg.VPush()],
					[sg.Button("Next", key="-NEXT1-"), sg.Button("Btn")]
					]
	graphs_layout = [
					[sg.VPush()],
					[sg.Button("Previous", key="-PREV0-"), sg.Button("Graphs", key="-GRAPHS-")]
					]

	return home_layout, graphs_layout