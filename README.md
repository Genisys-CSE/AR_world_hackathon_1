# Ar_World_Hackathon
AI-Powered Assistant By Team Code Rafters | AR World Hackathon  We developed an AI assistant integrating YOLO object detection, sign language recognition, AI conversations using Google Gemini API, and real-time translation with Tesseract OCR. Our goal: unify these technologies into a versatile, seamless assistant. 🚀

AI-Powered Assistant
Project Description
This project is an ambitious endeavor to integrate various cutting-edge AI models into a single, cohesive AI-powered assistant. Our main goal was to combine existing technologies to create a full-fledged assistant that can perform a range of tasks, including object detection, sign language recognition, AI-powered chat assistance, and real-time translation.

Main Objective
Our primary objective was to bring together various AI technologies into one unified assistant. While these technologies individually existed, our aim was to create a seamless experience by integrating them. We envisioned an AI assistant capable of performing multiple tasks, making it a versatile and powerful tool for users.

Features
YOLO Object Detection

Description: Utilizes the YOLO (You Only Look Once) model, fine-tuned with a custom dataset for accurate object detection.

Usage: Detects and identifies objects in real-time using a webcam feed.

Sign Language Detection

Description: Employs a pre-trained model for sign language recognition, sourced from GitHub.

Usage: Recognizes and translates sign language gestures into text, making communication more accessible.

AI Assistant using Google Gemini API

Description: A simple yet powerful AI assistant that leverages the Google Gemini API for conversational AI.

Usage: Engages in natural language conversations, providing responses and assistance based on user queries.

Real-Time Translator using Tesseract

Description: Integrates Tesseract OCR and translation APIs to provide real-time text translation.

Usage: Captures text from images, translates it to the desired language, and displays the translated text.

Front-End and Back-End Integration
We successfully developed the front end for the AI assistant, which includes user-friendly interfaces for each feature. However, we faced challenges in linking the models to the backend services, which prevented us from achieving full integration.

Technologies Used
YOLO for Object Detection

Custom Datasets for Fine-Tuning

Pre-Trained Sign Language Detection Model

Google Gemini API for AI Assistant

Tesseract OCR for Translation

Flask for Back-End Services

HTML, CSS, JavaScript for Front-End Development

Future Work
While the individual models and front-end interfaces are complete, we aim to resolve the integration challenges to create a seamless user experience. Our next steps include:

Successfully linking the backend services to the front-end interfaces.

Enhancing real-time performance and accuracy of the models.

Adding additional features and improving the user interface.
# Pre-Requistes Pip lib and modules:
pip install opencv-python numpy torch tensorflow keras speechrecognition pyttsx3 google-generativeai pytesseract requests langdetect
#How To Run:
1.Install the files in same directory
2.currenlty the backend is incomplete so to run we have to do it manually
3.Object Detection(Yolo) run- Work.py by command " python3 Work.py" in the same directory as of yolo
4. SIgnlanguage run - "python3 final_pred.py" in respected directory
5. ai assistant -  simply run the file
translaort run- simply run the file

#to view frontend:
open index.html to view the home page (Not Working)

Conclusion
This project showcases the potential of combining various AI technologies into a single assistant. Our vision is to create a versatile and powerful AI-powered assistant that can help users with a wide range of tasks. We believe that by overcoming the integration challenges, we can achieve our goal of developing a fully-fledged AI assistant.

Feel free to adjust any parts as needed. This description should provide a comprehensive overview of your project for your GitHub repository. If you have any more details you'd like to include, let me know! 🚀
