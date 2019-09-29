
import json
from datetime import datetime

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


# Instantiates a client
client = language.LanguageServiceClient()



def analysis(text):
  document = types.Document(
      content=text,
      type=enums.Document.Type.PLAIN_TEXT)

  # Detects the sentiment of the text
  sentiment = client.analyze_sentiment(document=document).document_sentiment
  return sentiment.score, sentiment.magnitude


########### main function ##################
def analysis_twitter_feeds(read_file_name, wirte_file_name, num_feeds):
  content=[]
  sentiment_score=[]
  sentiment_magnitude=[]
  time=[]

  f = open(read_file_name,"r")
  for i in range(num_feeds):
    content.append(f.readline())
    score,magnitude=analysis(content[i])
    now = datetime.now() # current date and time
    date=now.strftime("%m/%d/%Y_%H:%M:%S")
    time.append(date)
    sentiment_score.append(score)
    sentiment_magnitude.append(magnitude)
  f.close()

  data={}
  data["result"]=[]
  for i in range(num_feeds):
    data["result"].append({
      "text": content[i],
      "analysis_time":time[i],
      "sentiment_score":sentiment_score[i],
      "sentiment_magnitude":sentiment_magnitude[i]
      })

  with open(wirte_file_name, 'a') as outfile:
      json.dump(data, outfile)
  outfile.close()

#example 
read_file_name="result.txt"
wirte_file_name='data.txt'
num_feeds=3
analysis_twitter_feeds(read_file_name, wirte_file_name, num_feeds)
