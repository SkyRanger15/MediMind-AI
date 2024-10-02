import os
import PIL.Image
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import io
import json

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

with open('system_prompt.txt', 'r') as file:
    system_prompt = file.read()

with open('classification_prompt_structure.txt', 'r') as file:
    classify_model = file.read()

with open('classification_structure.json', 'r') as file:
    classification_structure = json.load(file)

generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-exp-0827",
  generation_config=generation_config,
  safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }
)

def analyze_image(uploaded_file):
    # Convert the uploaded file to a PIL Image
    image = PIL.Image.open(io.BytesIO(uploaded_file.getvalue()))

    response = model.generate_content([image, system_prompt])
    

    return image, response.text 