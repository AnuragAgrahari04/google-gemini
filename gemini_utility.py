import os
import json
import time
import io
from PIL import Image
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# working directory path
working_dir = os.path.dirname(os.path.abspath(__file__))

# path of config_data file
config_file_path = f"{working_dir}/config.json"
config_data = json.load(open(config_file_path))

# loading the GOOGLE_API_KEY
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# configuring google.generativeai with API key
genai.configure(api_key=GOOGLE_API_KEY)

def retry_generate_content(model, prompt, retries=3):
    for attempt in range(retries):
        try:
            return model.generate_content(prompt)
        except ResourceExhausted as e:
            if attempt < retries - 1:
                retry_delay = getattr(e, 'retry_delay', None)
                delay = retry_delay.seconds if retry_delay else 30
                print(f"[Attempt {attempt+1}] Rate limit hit. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise e

def load_gemini_pro_model():
    return genai.GenerativeModel("models/gemini-2.5-flash")

def gemini_pro_vision_response(prompt, image):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    # Convert image to bytes
    img_buffer = io.BytesIO()
    image.save(img_buffer, format="JPEG")
    image_bytes = img_buffer.getvalue()

    image_part = {
        "mime_type": "image/jpeg",
        "data": image_bytes
    }

    response = retry_generate_content(model, [prompt, image_part])
    return ''.join(part.text for part in response.parts if hasattr(part, 'text'))

def embeddings_model_response(input_text):
    embedding_model = "models/embedding-001"
    embedding = genai.embed_content(
        model=embedding_model,
        content=input_text,
        task_type="retrieval_document"
    )
    return embedding["embedding"]

def gemini_pro_response(user_prompt):
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = retry_generate_content(model, user_prompt)
    return ''.join(part.text for part in response.parts if hasattr(part, 'text'))