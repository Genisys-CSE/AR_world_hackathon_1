import speech_recognition as sr
import google.generativeai as genai

# Initialize the recognizer
recognizer = sr.Recognizer()

# Configure Gemini API with your provided API key
genai.configure(api_key="AIzaSyD6qSA56pWlNqZbVJVmjEeY-1Ve6v8RIKE")

def generate_summary(input_text):
    prompt = f"Summarize the following text in 40 words: {input_text}"
    try:
        # Assuming the correct method to generate text is `generate_text` directly from genai
        response = genai.generate_text(model="gemini-1.5-flash", prompt=prompt)
        summary = response.generations[0].text.strip()  # Correctly access the text attribute
        return summary
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "Error generating summary."

def main():
    # Use the microphone as the source
    with sr.Microphone() as source:
        print("Listening...")
        
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        # Capture the audio
        audio = recognizer.listen(source)
        
        try:
            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")

            # Send the text to Google Gemini API and get the summary
            summary = generate_summary(text)
            print(f"Summary: {summary}")
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        
        except sr.RequestError:
            print("Could not request results; check your internet connection.")

if __name__ == "__main__":
    main()
import speech_recognition as sr
import requests
import os

def recognize_speech():
    """Recognize speech from microphone"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

def summarize_text(text):
    """Send text to Gemini API for summarization"""
    API_KEY = os.getenv('AIzaSyD6qSA56pWlNqZbVJVmjEeY-1Ve6v8RIKE')  # Use environment variable
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
    
    payload = {
        "contents": [{"parts": [{"text": f"Summarize this in 40 words: {text}"}]}]
    }
    
    try:
        response = requests.post(url, json=payload)
        summary = response.json()['candidates'][0]['content']['parts'][0]['text']
        return summary
    except Exception as e:
        print(f"Error in API call: {e}")
        return None

def main():
    # Recognize speech
    spoken_text = recognize_speech()
    if spoken_text:
        # Get summary
        summary = summarize_text(spoken_text)
        if summary:
            print("Original Text:", spoken_text)
            print("Summary:", summary)

if __name__ == "__main__":
    main()