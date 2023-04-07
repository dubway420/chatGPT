from api_keys import api_key
import openai
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from io import BytesIO
import requests

city = "Manchester"
api_key = "40d5c3ea65d135d863cda3ca328175d7"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
weather_data = response.json()

description = weather_data['weather'][0]['description']

daily = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={1}&appid={api_key}"

response = requests.get(daily)
weather_data_daily = response.json()

print(weather_data_daily)

# mp3_fp = BytesIO()
# print(mp3_fp)

# openai.api_key = api_key

# def chatgpt_response(input):
#     playsound("Working.mp3")

    
#     completion = openai.ChatCompletion.create(
#       model="gpt-3.5-turbo",
#       messages=[
#         {"role": "user", "content": input}
#       ]
#     )

#     tts = gTTS(text=completion.choices[0].message.content, lang='en', tld="ca")
#     tts.write_to_fp(mp3_fp)
  


# r = sr.Recognizer()

# while(1):   
     
#     # Exception handling to handle
#     # exceptions at the runtime
#     try:
         
#         # use the microphone as source for input.
#         with sr.Microphone() as source2:
             
#             # wait for a second to let the recognizer
#             # adjust the energy threshold based on
#             # the surrounding noise level
#             r.adjust_for_ambient_noise(source2, duration=0.2)
             
#             #listens for the user's input
#             audio2 = r.listen(source2)
             
#             # Using google to recognize audio
#             MyText = r.recognize_google(audio2)
#             MyText = MyText.lower()
 
#             # print("Did you say ", MyText)
#             chatgpt_response(MyText)
             
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
         
#     except sr.UnknownValueError:
#         print("unknown error occurred")



