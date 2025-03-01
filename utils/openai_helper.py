import streamlit as st
import json
from openai import OpenAI

# Initialize OpenAI client using Streamlit Secrets
api_key = st.secrets["OPENAI_API_KEY"]
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