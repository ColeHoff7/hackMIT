import json
import sys
#import recording
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import ToneAnalyzerV3

def parse_speech(filearg):
   with open(join(dirname(__file__), filearg), 'rb') as audio_file:
       text = json.dumps(speech_to_text.recognize(audio_file, content_type='audio/wav', continuous = True, timestamps=True), indent=2)
       parsed = json.loads(text)
       p1 = ""
       for x in parsed['results']:
         p2 = x['alternatives'][0]['transcript']  
         p1+=p2

       return p1

def parse_tone(speech):
   print(json.dumps(tone_analyzer.tone(text=speech), indent=2))

if __name__ == "__main__":
   speech_to_text = SpeechToTextV1(
       username='e28da131-47ff-49b2-bb21-9d78290cd945',
       password='noFUouvEAxKn',
       x_watson_learning_opt_out=False
   )

   tone_analyzer = ToneAnalyzerV3(
    username='b66c6065-462b-4eab-90e4-5cb59ec8289b',
    password='47XThYg7buM5',
    version='2016-02-11')

   #recording.init()
   #print("finished recording")
   speech = parse_speech(sys.argv[1])
   #print(speech)
   parse_tone(speech)
