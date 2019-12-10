import IPython
import pandas as pd
import math
import time
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

startIdx = 41550
# perRequest = 600
# numRound = 10

# # total 42181

# for count in range(numRound):
# 	endIdx = startIdx+perRequest

# 	for i in range(startIdx,endIdx):
# 		print(i)	
# 		line = data["line_text"][i]	
# 		if(isinstance(line, str)):
# 			document = getSentiment(line)
# 			# Detects the sentiment of the text
# 			sentiment = client.analyze_sentiment(document=document).document_sentiment
# 			data["sentiment score"][i] = sentiment.score

# 	print("Finished Round: "+str(count+1))
# 	data.to_excel('topCast.xlsx', index=False)	# every round update the excel file once
# 	print("File Updated !")
# 	startIdx = endIdx
# 	time.sleep(60) # pause 30s for each round of requests

# final round 
for i in range(startIdx,len(data["line_text"])):
	print(i)	
	line = data["line_text"][i]	
	if(isinstance(line, str)):
		document = getSentiment(line)
		# Detects the sentiment of the text
		sentiment = client.analyze_sentiment(document=document).document_sentiment
		data["sentiment score"][i] = sentiment.score

	
data.to_excel('topCast.xlsx', index=False)	# every round update the excel file once
print("File Updated !")


# small testing purpose
# i = 36144
# line = data["line_text"][i]	
# line = "maddening!"
# print(line)
# document = getSentiment(line)
# sentiment = client.analyze_sentiment(document=document).document_sentiment
# data["sentiment score"][i] = sentiment.score			





