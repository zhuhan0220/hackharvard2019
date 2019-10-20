import io
import os

#imports the Google Cloud client liobrary
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.oauth2 import service_account

#instantiates a client
credentials=service_account.Credentials.from_service_account_file('/Users/hanzhu/Documents/Hackathon/hackathon-f71ecbf7cb03.json')
client=speech.SpeechClient(credentials=credentials)

print(client)

#The name of the audio file to transcribe
file_name=os.path.join(os.path.dirname(__file__),'resources','Google_Gnome.wav')

print(file_name)

#loads the audio into memory
with io.open(file_name,"rb") as audio_file:
    content=audio_file.read()
    audio=types.RecognitionAudio(content=content)

config=types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

#Detects speech in the audio file
response=client.recognize(config, audio)

for result in response.results:
    print("Transcript:{}".format(result.alternatives[0].transcript))