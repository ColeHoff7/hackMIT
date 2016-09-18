import json
import recording
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

if __name__ == "__main__":
   speech_to_text = SpeechToTextV1(
       username='e28da131-47ff-49b2-bb21-9d78290cd945',
       password='noFUouvEAxKn',
       x_watson_learning_opt_out=False
   )  
   
   recording.init();
   parse-speech();

def parse-speech():
   with open(join(dirname(__file__), 'demo.wav'), 'rb') as audio_file:
       text = json.dumps(speech_to_text.recognize(audio_file, content_type='audio/wav', continuous = True, timestamps=True), indent=2))
       print(text.alternatives);     


