# # from urllib import response
# # from flask import Flask, render_template, request, jsonify 
# # from openai import OpenAI
# # import speech_recognition
# # import pyaudio
# # from pathlib import Path
# # from dash import Dash, html, dcc, callback, Input, Output, State, callback
# # import pyttsx3
# # from gtts import gTTS
# # import os
# # # from playsound import playsound
  
# # app = Flask(__name__) 
  
# # # OpenAI API Key 

# # client = OpenAI(api_key = '')


# # def audio(prompt):
# #     speech_file_path="/Users/Adrian/hgpfinal/output.mp3"
# #     with client.audio.speech.with_streaming_response.create(
# #         model="tts-1",
# #         voice="alloy",
# #         input=prompt,
# #     ) as response:
# #         response.stream_to_file(speech_file_path)



# # wakeword = "Goober"
# # opener = "How can I help you today"

# # myspeaker = pyttsx3.init()
# # # myspeaker.say("I will speak this text")
# # recognizer = speech_recognition.Recognizer()



# # with speech_recognition.Microphone() as source:
# #     audio(opener)
# # # while True:
# # #      # Increment session ID for the next interaction
# # #     #Enables Mircophone
# # #     with speech_recognition.Microphone() as source:
# # #         myspeaker.runAndWait()


# # def get_completion(prompt): 
# #     messages = [{"role": "system", "content": " I am your virtual assistant "},
# #             {"role": "system", "content": prompt}
# #             ]
# #     print(prompt) 
# #     query = client.chat.completions.create( 
# #         model="gpt-4o", 
# #         messages= messages,
# #         max_tokens=1024, 
# #         n=1, 
# #         stop=None, 
# #         temperature=0.5, 
# #     ) 
  
# #     answer = query.choices[0].message.content.strip() 
# #     return answer
  
# # @app.route("/", methods=['POST', 'GET']) 
# # def query_view(): 
# #     if request.method == 'POST': 
# #         print('step1') 
# #         prompt = request.form['prompt'] 
# #         answer = get_completion(prompt) 
# #         print(answer) 
  
# #         return jsonify({'response': answer}) 
# #     return render_template('index.html') 
# #     text = str(answer)
# #     # tts =gTTS(text=text, lang= 'en')
# #     speech_file_path = Path(__file__).parent / "output.mp3"
# #     file_path = "null" 
# #     file_path = "output.mp3"
# #     myobj = gTTS(text= response, lang= 'en', slow= False)
# #     output_file = "/Users/Adrian/hgpfinal/steve_jobs_speech_generated_hd.mp3"
# #     tts.save(output_file)

# # #myobj.save("output.mp3")

# # os.system("start output.mp3")
# # if __name__ == "__main__": 
# #     app.run(debug=True) 


# # # def playsound (response):
# # #     playsound('/Users/Adrian/hgpfinal/steve_jobs_speech_generated_hd.mp3')
# # #     print('thinking')

# # # playsound()




# from flask import Flask, render_template, request, jsonify
# from openai import OpenAI
# import pyttsx3
# from pathlib import Path

# app = Flask(__name__)

# # Initialize OpenAI client
# client = OpenAI(api_key='')

# # Initialize pyttsx3 for text-to-speech
# myspeaker = pyttsx3.init()

# # Function to convert text to speech using OpenAI
# def audio(prompt):
#     speech_file_path = "/Users/Adrian/hgpfinal/output.mp3"
#     with client.audio.speech.with_streaming_response.create(
#         model="tts-1",
#         voice="alloy",
#         input=prompt,
#     ) as response:
#         response.stream_to_file(speech_file_path)

# # Function to convert text to speech using pyttsx3
# def speak(text, rate=150):  # Adjust rate as needed (default is 150)
#     myspeaker.setProperty('rate', rate)
#     myspeaker.say(text)
#     myspeaker.runAndWait()
#     speak()

# # Function to get AI completion from OpenAI
# def get_completion(prompt):
#     messages = [{"role": "system", "content": "I am your virtual assistant"},
#                 {"role": "system", "content": prompt}
#                 ]
#     query = client.chat.completions.create(
#         model="gpt-4o",
#         messages=messages,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     answer = query.choices[0].message.content.strip()
#     return answer

# # Flask route for handling POST requests
# @app.route("/", methods=['POST', 'GET'])
# def query_view():
#     if request.method == 'POST':
#         prompt = request.form['prompt']
#         answer = get_completion(prompt)
#         # Convert the answer to speech using pyttsx3 (adjust rate if needed)
#         speak(answer, rate=150)  # Adjust rate as needed (150 is a default)
#         return jsonify({'response': answer})
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)
