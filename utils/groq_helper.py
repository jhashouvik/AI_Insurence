import json
import os
from groq import Groq

# Initialize Groq client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Load API key from environment variable
groq_client = Groq(api_key=GROQ_API_KEY)

def process_user_input(query):
    """
    Process natural language input using Groq's Llama 3.3-70b model.
    """
    try:
        response = groq_client.chat.completions.create(
            model="llama3-70b-8192",  # Use the Llama 3.3-70b model
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