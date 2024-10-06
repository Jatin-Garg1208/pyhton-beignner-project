import os
import google.generativeai as genai
from config import API_KEY  # Import the API key from config.py
import speech_to_text as s
genai.configure(api_key=API_KEY)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="give text and want 10 quiz with 4 option and return data in json and give option in a b c d \n\n\n",
)

chat_session = model.start_chat(
  history=[
  ]
)
response = chat_session.send_message(s.result)

print(response.text)