from google import genai
from google.genai import types # For setting config
import os
import dotenv

dotenv.load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Api testing
def test_api(prompt):
    response = client.models.generate_content(

        # Set the config for the model
        config=types.GenerateContentConfig(
            max_output_tokens=50,
            temperature=0.7,
            top_p=0.9,
            top_k=50,
            response_mime_type="text/plain"
        ),
        
        # Set the model
        model="gemini-2.0-flash",
        
        # Set the prompt
        contents=[prompt]
        
        )
    return (response.text)