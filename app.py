import os
from google import genai
from prompts import BASELINE_PROMPT, IMPROVED_PROMPT

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=api_key)

customer_email = """
Subject: Refund me immediately

Your company is ridiculous. My order arrived late and I want a full refund right now.
If you do not refund me today, I will report your business everywhere online.
"""

def run_model(prompt: str, email_text: str, model_name: str = "gemini-3.1-flash-lite"):
    full_input = f"{prompt}\n\nCustomer email:\n{email_text}"
    response = client.models.generate_content(
        model=model_name,
        contents=full_input,
    )
    return response.text

print("========== CUSTOMER EMAIL ==========")
print(customer_email)

print("\n========== BASELINE OUTPUT ==========")
baseline_output = run_model(BASELINE_PROMPT, customer_email)
print(baseline_output)

print("\n========== IMPROVED OUTPUT ==========")
improved_output = run_model(IMPROVED_PROMPT, customer_email)
print(improved_output)