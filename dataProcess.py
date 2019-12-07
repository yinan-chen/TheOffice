import IPython
import pandas as pd
import re

# clean line with "���"
# replace with "'" if 're, 've, 'll,'m','s','d','t' 
# else replace with "."
def cleanLine(line):
    line = str(line)
    x = re.search(r'���[re|ve|ll|m|s|t|d]', line)
    if(x):
        line = line.replace("���","'")
    else:
        line = line.replace("���",".")
        
    # extract action out from quotes
    x = re.findall(r'\[.*?\]', line)
    if(len(x) != 0):
        return re.sub(r'\s*\[.*?\]\s*',"",line)
    else:
        return line

def cleanName(name):
	# extract action out from names
    x = re.findall(r'\[.*?\]', name)
    if(len(x) != 0):
        return re.sub(r'\s*\[.*?\]\s*',"",name)
    else:
        return name   

#load dataset
data = pd.read_excel("the-office-lines.xlsx")
data["line_text"] = data["line_text"].apply(cleanLine)
data["speaker"] = data["speaker"].apply(cleanName)

data.to_excel('output.xlsx', index=False)







