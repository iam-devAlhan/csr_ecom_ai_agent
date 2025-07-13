import requests
import json
import os
import re
from dotenv import load_dotenv

load_dotenv()

shopify_store = os.getenv("SHOPIFY_STORE_NAME")
shopify_admin_access_token = os.getenv("SHOPIFY_ADMIN_ACCESS")

shopify_api = f"https://{shopify_store}.myshopify.com/admin/api/2023-01/products.json"

headers = {
    "X-Shopify-Access-Token": shopify_admin_access_token
}

def clean_html_from_description(raw: str) -> str:
    clean_text = re.sub(r"<[^>]+>", "", raw)
    return clean_text.strip()


def get_all_shopify_products():
    response = requests.get(shopify_api, headers=headers).json()
    products = response["products"]

    cleaned_data = []
    path = "clean_products.json"
    for product in products:
        variant = product["variants"][0]
        cleaned = {
            "title": product["title"],
            "description": clean_html_from_description(product["body_html"]),
            "price": float(variant.get("price", 0)),
            "sku": variant.get("sku", "N/A"),
            "inventory": variant.get("inventory_quantity", 0),
            "image": product.get("image", {}).get("src"),
            "url": f"https://{shopify_store}.myshopify.com/products/{product['handle']}"
        }
        cleaned_data.append(cleaned)
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

    print(f"{len(cleaned_data)} products saved to {path}")
