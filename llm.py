import os
from google import genai
from google.genai import types

os.environ["GEMINI_API_KEY"] = os.environ.get("GEMINI_API_KEY", "YOUR_KEY_HERE")

def analyze_vulnerability(target_url):
    client = genai.Client()
    system_instruction = (
        "You are an elite Cybersecurity Expert with an extensive knowledge graph of "
        "web application security. Provide a structured, legal, and ethical methodology "
        "to test the given target URL."
    )
    user_prompt = f"Develop a preliminary vulnerability testing plan for the target URL: {target_url}"
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.3,
            ),
        )
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if _name_ == "_main_":
    analyze_vulnerability("http://example.com")
