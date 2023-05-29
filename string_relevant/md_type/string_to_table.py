a = """Source	DF	Adj SS	Adj MS	F-Value	P-Value
Regression	4	47.9096	11.9774	18.17	0.000
  Conc	1	3.9232	3.9232	5.95	0.022
  Ratio	1	31.0216	31.0216	47.07	0.000
  Temp	1	3.6031	3.6031	5.47	0.027
  Time	1	1.9839	1.9839	3.01	0.094
Error	27	17.7953	0.6591	 	 
  Lack-of-Fit	25	17.7836	0.7113	121.94	0.008
  Pure Error	2	0.0117	0.0058	 	 
Total	31	65.7049	 	 	 """


import pyperclip
def get_table_from_string():
    while True:
        s = pyperclip.waitForNewPaste()
        s_list = s.split('\n')
        s_list = [line.strip('\r') for line in s_list if line.strip() != '']
        print(s_list)
        s = '\n'.join(s_list)
        print(s)
        s = s.replace('\t', ' | ')
        s = s.replace('\n', ' | \n| ')
        s = '| ' + s + ' |'
        first_line = s[:s.find('\n')+1]
        num_cols = first_line.count('|')-1
        divide_line = '| ' + ' | '.join(['---'] * num_cols) + ' |\n'
        s = first_line + divide_line + s[s.find('\n')+1:]
        pyperclip.copy(s)

get_table_from_string()