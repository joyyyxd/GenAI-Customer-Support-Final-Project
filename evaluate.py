import json
import os
from google import genai
from prompts import BASELINE_PROMPT, IMPROVED_PROMPT

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=api_key)

def run_model(prompt: str, email_text: str, model_name: str = "gemini-3.1-flash-lite"):
    full_input = f"{prompt}\n\nCustomer email:\n{email_text}"
    response = client.models.generate_content(
        model=model_name,
        contents=full_input,
    )
    return response.text

with open("test_cases.json", "r", encoding="utf-8") as f:
    test_cases = json.load(f)

for case in test_cases:
    print("\n" + "=" * 60)
    print("CASE ID:", case["id"])
    print("EMAIL:")
    print(case["email"])

    print("\n--- BASELINE ---")
    print(run_model(BASELINE_PROMPT, case["email"]))

    print("\n--- IMPROVED ---")
    print(run_model(IMPROVED_PROMPT, case["email"]))