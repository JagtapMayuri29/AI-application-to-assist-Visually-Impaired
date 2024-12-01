import streamlit as st
import google.generativeai as genai
from PIL import Image
import pytesseract
import os
from langchain_google_genai import GoogleGenerativeAI
from gtts import gTTS
import tempfile

# Initialize Google Generative AI with API Key
GEMINI_API_KEY = "______________"  # Replace with your valid API key
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
llm = GoogleGenerativeAI(model="gemini-1.5-pro", api_key=GEMINI_API_KEY)

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Streamlit UI elements
st.set_page_config(layout="wide")
st.title("🤖:orange[AI-Powered Assistant for Visually Impaired Individuals]⚙️")
st.subheader(':blue[***Helping visually impaired individuals with image-based analysis.***]')
st.markdown("""
This project aims to leverage Generative AI to assist visually impaired individuals in perceiving
and interacting with their surroundings.Visually impaired individuals often face challenges in understanding
their environment, reading visual content, and performing tasks that rely on sight.
""")
st.markdown("### :blue[Purpose:]")
st.markdown("""The app is designed to enhance the independence and quality of life of visually impaired individuals by:
Providing accurate descriptions of their surroundings or specific objects.
Extracting and vocalizing text from visual sources like documents, signs, or labels.
Offering voice-guided interaction for seamless, hands-free usability.
""")

# Streamlit Sidebar
st.markdown(
    """
    <style>
    /* Sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #E6E6FA;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Add an image to the sidebar
st.sidebar.image(
    r"C:\Users\Acer\Desktop\Innomatics\Regex Project\project_1\Gen ai\ai 1.jpg", 
    caption="Empowering Vision",  
    use_container_width=True 
)

st.sidebar.title(":green[Welcome to AI Vision]")
st.sidebar.markdown("### 💡 :red[Content:]")
st.sidebar.markdown("""
- **Scene Understanding**: 
  Get detailed descriptions of uploaded images.
  
- **Text Recognition**: 
  Extract text from images, such as signs, documents, or labels.
  
- **Text-to-Speech**: 
  Listen to extracted text or scene descriptions for better accessibility.
  """)
st.sidebar.markdown("### 🌟 :red[How It Works:]")
st.sidebar.markdown("""
1. Upload an image to analyze.
2. Use buttons to extract scene descriptions or text.
3. Enable audio playback for text-to-speech support.
""")

# Apply custom CSS for styling file uploader label 
st.markdown(
    """
    <style>
    .file-uploader-label {
        font-size: 24px;  
        font-weight: bold;  
        color: green; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Apply custom CSS for styling for Select functionality
st.markdown(
    """
    <style>
    /* Style the selectbox label */
    label[for="Select Functionality"] {
        font-size: 18px; /* Adjust font size */
        font-weight: bold; /* Make it bold */
        color: green; /* Change label color */
    }

    /* Style the dropdown box */
    div[data-baseweb="select"] {
        background-color: #f0f8ff; /* Light blue background */
        border: 2px solid #4caf50; /* Green border */
        border-radius: 8px; /* Rounded corners */
        padding: 5px; /* Add padding inside the box */
    }

    /* Style the dropdown options */
    ul[role="listbox"] li {
        font-size: 16px; /* Option font size */
        color: #333; /* Option text color */
        background-color: #fff; /* Option background color */
        padding: 10px; /* Add padding for options */
        border-bottom: 1px solid #ddd; /* Divider between options */
    }

    /* Highlighted option style on hover */
    ul[role="listbox"] li:hover {
        background-color: #cfe2f3; /* Light blue hover background */
        color: #000; /* Text color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Functions
def generate_scene_description(prompt, image_data):
    """Generates a scene description using Google Generative AI."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content([user_prompt, image_data])
        return response.text
    except Exception as e:
        return f"Error: {e}"

def extract_text_from_image(image):
    """Extracts text from the given image using OCR."""
    try:
        return pytesseract.image_to_string(image)
    except Exception as e:
        return f"Error during OCR: {e}"

def generate_contextual_guidance(prompt,extracted_text):
    """Generate task-specific guidance using Google Generative AI."""
    try:
        input_text = f"{prompt}\nExtracted text: {extracted_text}"
        response = llm.generate(prompts=[input_text])  
        # Extract the generated text
        if response.generations and len(response.generations[0]) > 0:
            guidance_text = response.generations[0][0].text 
            return guidance_text
        else:
            return "No guidance could be generated. Please try again."
    except Exception as e:
        return f"Error: {e}"  

def text_to_speech(text):
    """Converts the given text to speech using gTTS."""
    try:
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            tts.save(temp_audio.name)
            st.audio(temp_audio.name, format="audio/mp3")
    except Exception as e:
        st.error(f"Error during Text-to-Speech: {e}")

def prepare_image(uploaded_file):
    """Prepares the uploaded image for processing."""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return {
            "mime_type": uploaded_file.type,
            "data": bytes_data,
        }
    else:
        st.warning("No file uploaded.")
        return None

# Input Prompt for Scene Understanding
user_prompt = """
You are an AI assistant providing scene descriptions to assist visually impaired individuals. Analyze the image and provide a detailed description, ensuring clarity and relevance. Include the following:
Overall Scene: Briefly describe the setting or environment (e.g., indoors, outdoors, nature, urban, etc.).
Location: Give the Location of image.
Objects and Elements: List and describe key objects, their positions, and notable details.
People or Activities: If people are present, mention their appearance, actions, or interactions.
Colors and Lighting: Highlight dominant colors, lighting conditions (e.g., bright, dim), and mood.
Accessibility Suggestions: Offer actionable suggestions or precautions if applicable (e.g., "There are stairs ahead" or "Objects on the floor may be a tripping hazard").
"""

# Main App Logic

# Display a custom label above the file uploader
st.markdown('<p class="file-uploader-label">Upload an image for analysis...</p>', unsafe_allow_html=True)


#File Upload
uploaded_file = st.file_uploader(':red[***"Choose an image......"***]', type=["jpg", "jpeg", "png"])
if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
   
    
# Prepare image data
if uploaded_file:
    image_data = prepare_image(uploaded_file)

# Functionality selection with colors
    functionality = st.selectbox(
    "Select Functionality", 
    ["Get Scene Description", "Extract Text from Image", "Convert Text to Speech","Context-Specific Guidance"],
    index=None,
    placeholder="Select function...",
   )
    
    # Scene Understanding
    if functionality == "Get Scene Description":
        st.markdown("<h3 style='color: blue;'>You selected 'Describe Image'.</h3>", unsafe_allow_html=True)
        with st.spinner("👨‍🦯‍➡️ Analyzing the image... Please wait...."):
            if image_data:
                description = generate_scene_description(user_prompt, image_data)
                st.success("### 🔍 Scene Description")
                st.write(description)
                 # Convert scene description to speech
                st.subheader("🔊 Play Scene Description")
                text_to_speech(description)
            else:
                st.warning("Could not process the image. Please try again.")

    # Extract Text
    elif functionality == "Extract Text from Image":
        st.markdown("<h3 style='color: green;'>You selected 'Extract Text'.</h3>", unsafe_allow_html=True)
        with st.spinner("Extracting text from the image..."):
            extracted_text = extract_text_from_image(image)
            if extracted_text.strip():
                st.success("###  📝Text Extracted Successfully")
                st.text_area("Extracted Text", extracted_text, height=150)
            else:
                st.warning("No text found in the image. 😔.")

    # Text-to-Speech
    elif functionality == "Convert Text to Speech":
        st.markdown("<h3 style='color: orange;'>You selected 'Text to Speech'.</h3>", unsafe_allow_html=True)
        with st.spinner("Converting text to speech..."):
            extracted_text = extract_text_from_image(image)
            if extracted_text.strip():
                text_to_speech(extracted_text)
                st.success("Text-to-Speech Conversion Completed!")
            else:
                st.warning("No text available for speech.")

    # Provide context-specific guidance
    elif functionality == "Context-Specific Guidance":
        with st.spinner("Generating context-specific guidance..."):
            extracted_text = extract_text_from_image(image)
            prompt = """
            You are an AI assistant helping visually impaired individuals. Based on the provided image:
            1. Analyze the extracted text for relevance.
            2. Provide context-specific recommendations based on the text.
            3. Suggest actions or precautions for the visually impaired.
            """
            guidance = generate_contextual_guidance(prompt, extracted_text)
            if guidance:
                st.success("Context-Specific Guidance:")
                st.write(guidance)
                st.subheader("🔊 Listen to Guidance")
                text_to_speech(guidance)
            else:
                st.warning("Could not generate guidance.")
