from dotenv import load_dotenv
import os
import json
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Debug: Print the API key to verify it's loaded
api_key = os.getenv("OPENAI_API_KEY")
#print("Loaded OpenAI API Key:", api_key)

# Initialize OpenAI client
if not api_key:
    raise ValueError("OpenAI API key not found in .env file. Please check your configuration.")

client = OpenAI(api_key=api_key)

def process_user_input(query):
    """
    Process natural language input using OpenAI.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """Extract insurance search parameters from the user query.
                    Return JSON with fields: name, age, gender, lifestyle.
                    Lifestyle should be one of: Healthy, Average, Sedentary"""
                },
                {"role": "user", "content": query}
            ],
            response_format={"type": "json_object"}
        )

        # Parse the JSON string into a dictionary
        parsed_data = json.loads(response.choices[0].message.content)
        return parsed_data
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse response: {str(e)}"}
    except Exception as e:
        return {"error": f"Failed to process input: {str(e)}"}