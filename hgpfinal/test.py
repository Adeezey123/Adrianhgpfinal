from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import pyttsx3
import threading
from pathlib import Path
import assemblyai as aai 

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key='')

aai.settings.api_key = "21f49f8871944a4d83a14f9919309739"

transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
print(transcript.text)
# Create thread-local storage for pyttsx3 instances
tls = threading.local()

# Function to convert text to speech using OpenAI
def audio(prompt):
    speech_file_path = "/Users/Adrian/hgpfinal/output.mp3"
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=prompt,
    ) as answer:
        answer.stream_to_file(speech_file_path)

# Function to initialize pyttsx3 for the current thread
def get_speaker():
    if not hasattr(tls, 'speaker'):
        tls.speaker = pyttsx3.init()
    return tls.speaker

# Function to convert text to speech using pyttsx3
def speak(text, rate=150):
    myspeaker = get_speaker()
    myspeaker.setProperty('rate', rate)
    myspeaker.say(text)
    myspeaker.runAndWait()
    if myspeaker._inLoop:
        myspeaker.endLoop()

# Function to get AI completion from OpenAI
def get_completion(prompt):
    messages = [{"role": "system", "content": "I am your virtual assistant"},
                {"role": "system", "content": prompt}
                ]
    query = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = query.choices[0].message.content.strip()
    return answer

# Flask route for handling POST requests
@app.route("/", methods=['POST', 'GET'])
def query_view():
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = get_completion(prompt)
        speak(answer, rate=175)  # Adjust rate as needed
        return jsonify({'response': answer})
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


