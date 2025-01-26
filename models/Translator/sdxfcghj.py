import cv2
import numpy as np
import pytesseract
import requests
from langdetect import detect
import tkinter as tk
from tkinter import Button

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# MyMemory Translation API URL
MYMEMORY_API_URL = "https://api.mymemory.translated.net/get"

def translate_text(text, target_lang='en'):
    try:
        source_lang = detect(text)
    except:
        return "Error: Unable to detect language"
    
    payload = {
        'q': text,
        'langpair': f'{source_lang}|{target_lang}'
    }
    response = requests.get(MYMEMORY_API_URL, params=payload)
    if response.status_code == 200:
        result = response.json()
        if 'responseData' in result and 'translatedText' in result['responseData']:
            return result['responseData']['translatedText']
        else:
            return "Error: Translation key not found"
    else:
        return "Error: Translation service unavailable"

def capture_and_process_frame():
    ret, frame = cap.read()
    if not ret:
        print("Error capturing frame")
        return

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Captured Frame', gray)

    # Extract text from the frame using OCR
    detected_text = pytesseract.image_to_string(gray).strip()
    print(f"Detected text: {detected_text}")

    if detected_text:
        # Send the detected text for translation
        translated_text = translate_text(detected_text)
        print(f"Translated text: {translated_text}")

        # Display the translated text on the frame
        cv2.putText(frame, translated_text, (10, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Real-Time Text Detection and Translation', frame)

def main():
    global cap
    cap = cv2.VideoCapture(0)

    # Create a tkinter window
    root = tk.Tk()
    root.title("Text Detection and Translation")

    def on_exit():
        # Release the webcam and close windows
        cap.release()
        cv2.destroyAllWindows()
        root.destroy()

    # Add an Exit button to the tkinter window
    exit_button = Button(root, text="Exit", command=on_exit)
    exit_button.pack()

    def update_frame():
        capture_and_process_frame()
        root.after(1, update_frame)

    update_frame()
    root.mainloop()

if __name__ == "__main__":
    main()
