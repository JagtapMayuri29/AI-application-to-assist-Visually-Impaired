# 🤖 AI-application-to-assist-Visually-Impaired

***This project aims to leverage Generative AI to assist visually impaired individuals in perceiving
and interacting with their surroundings.Visually impaired individuals often face challenges in understanding
their environment, reading visual content, and performing tasks that rely on sight.***

##  ⚙️ Key Features ##
### Scene Understanding ###

Provides a detailed description of an image or scene to help users understand their surroundings.
Detects objects, people, and activities in the scene.
Suggests actions or precautions based on the scene.

### Text Recognition (OCR) ###

Extracts text from images of documents, books, signs, or product labels.
Reads handwritten or printed text aloud using text-to-speech (TTS) technology.

### Text-to-Speech Conversion ###

Converts extracted text or scene descriptions into audible speech.
Offers multi-language support for global accessibility.

## Core Technologies ##

### 1.Generative AI (Google Generative AI) :  
Models like OpenAI's GPT or Google's Gemini provide advanced scene understanding and contextual descriptions.
### 2.Streamlit :  
Streamlit is an open-source app framework used for creating web-based data applications with Python. It is simple to use and allows developers to build interactive web applications 
### 3.Langchain  : 
LangChain is a framework designed to help developers build applications powered by large language models (LLMs)

## Tools and Technologies Used ##

### Streamlit: 
For developing a user-friendly interface.
### Google Generative AI (Gemini 1.5): 
For generating scene descriptions and contextual guidance.
### Langchain : 
Used LangChain's GoogleGenerativeAI integration to query Gemini for scene descriptions based on the image content. Combine OCR output with LangChain to provide enhanced and structured prompts to the AI for contextual guidance.
### Tesseract OCR:
For extracting text from images.
### gTTS (Google Text-to-Speech): 
For converting text into speech.
### Pillow: 
For image preprocessing and manipulation.

