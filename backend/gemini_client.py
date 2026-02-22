import google.generativeai as genai
import logging
from config.settings import GEMINI_API_KEY

logging.basicConfig(
    filename="logs/app.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

genai.configure(api_key = GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(prompt:str) -> str:
    """ sends prompt to Gemini and returns response text. """
    try:
        logging.info("Sending request to Gemini API")
        response = model.generate_content(
            prompt,
            generation_config={
                "max_output_tokens": 2000,
                "temperature": 0.7
                }
)
        logging.info("Received response from Gemini API")
        
        return response.text 
    except Exception as e:
        logging.error(f"Error in Gemini API call:{str(e)}")
        return "Sorry, I am facing technical difficukties. please try again."