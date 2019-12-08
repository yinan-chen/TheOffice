# Account Key Path: /Untitled/Users/Sherry/Desktop/accountKey.json
# export GOOGLE_APPLICATION_CREDENTIALS="accountKey.json"

import IPython
import pandas as pd
import math
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def getSentiment(line):
	text = line
	document = types.Document(
    	content=text,
    	type=enums.Document.Type.PLAIN_TEXT)
	return document

# Instantiates a client
client = language.LanguageServiceClient()

#load dataset
data = pd.read_excel("topCast.xlsx")

for i in range(1650,2550):
	print(i)	
	line = data["line_text"][i]	
	if(isinstance(line, str)):
		document = getSentiment(line)
		# Detects the sentiment of the text
		sentiment = client.analyze_sentiment(document=document).document_sentiment
		data["sentiment score"][i] = sentiment.score

data.to_excel('topCast_sentiment.xlsx', index=False)