import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_groq_response(user_query: str) -> str:
    try:
        with open("shopify/clean_products.json", "r", encoding="utf-8") as f:
            products = json.load(f)

        prompt = f"""
        You are EcomAgent, an ecommerce assistant.
        Here are the products:
        {products}

        The user says: "{user_query}"

        Respond helpfully by mentioning relevant products, cheapest and most expensive items. Keep it short.
        """

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are an ecommerce bot."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

        # ✅ Debug: Print response for safety
        print("Groq Raw Response:", response.text)

        if response.status_code != 200:
            return f"Groq API Error: {response.status_code} - {response.text}"

        result = response.json()
        return result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"Groq API Error: {e}"
